// SPDX-License-Identifier: BUSL-1.1
pragma solidity 0.8.25;

import {StakingVaultStorageLib} from "./StakingVaultStorage.sol";
import {IStakingVault} from "../interfaces/IStakingVault.sol";
import {Validator} from "gokite-contracts/contracts/validator-manager/interfaces/IACP99Manager.sol";

/**
 * @title StakingVaultInternals
 * @notice Shared internal functions for StakingVault and StakingVaultOperations
 * @dev Library functions are inlined by the compiler, so no gas overhead.
 *      These functions read from the shared ERC-7201 namespaced storage.
 */
library StakingVaultInternals {
    // ============================================
    // View Functions
    // ============================================

    /**
     * @notice Get the current epoch number
     * @return epoch Current epoch based on epochStartTime and epochDuration
     */
    function getCurrentEpoch() internal view returns (uint256 epoch) {
        StakingVaultStorageLib.StakingVaultStorage storage $ = StakingVaultStorageLib._getStorage();
        return (block.timestamp - $.epochStartTime) / $.epochDuration;
    }

    /**
     * @notice Get total pooled stake (balance + delegated + validator stake - liabilities)
     * @return stake Total pooled stake amount
     */
    function getTotalPooledStake() internal view returns (uint256 stake) {
        StakingVaultStorageLib.StakingVaultStorage storage $ = StakingVaultStorageLib._getStorage();
        uint256 totalAssets = $.vaultAccountedBalance
            + $.totalDelegatedStake
            + $.totalValidatorStake;
        uint256 liabilities = $.pendingWithdrawalStake + $.totalAccruedOperatorFees
            + $.pendingProtocolFees + $.totalEscrowedWithdrawals;
        if (totalAssets > liabilities) {
            return totalAssets - liabilities;
        }
        return 0;
    }

    /**
     * @notice Get available stake (liquid balance minus reserved amounts)
     * @return stake Available stake amount
     */
    function getAvailableStake() internal view returns (uint256 stake) {
        StakingVaultStorageLib.StakingVaultStorage storage $ = StakingVaultStorageLib._getStorage();
        uint256 balance = $.vaultAccountedBalance;
        uint256 reserved = $.claimableWithdrawalStake + $.totalAccruedOperatorFees
            + $.pendingProtocolFees + $.totalEscrowedWithdrawals;
        if (balance > reserved) {
            return balance - reserved;
        }
        return 0;
    }

    /**
     * @notice Get minimum stake duration from the staking manager
     * @return minStakeDuration Minimum stake duration in seconds
     */
    function getMinimumStakeDuration() internal view returns (uint64 minStakeDuration) {
        StakingVaultStorageLib.StakingVaultStorage storage $ = StakingVaultStorageLib._getStorage();
        (bool success, bytes memory data) = address($.stakingManager).staticcall(
            abi.encodeWithSelector(StakingVaultStorageLib.SEL_GET_STAKING_MANAGER_SETTINGS)
        );
        if (!success || data.length < 128) {
            revert IStakingVault.StakingVault__StakingManagerCallFailed();
        }
        assembly {
            minStakeDuration := mload(add(data, 128))
        }
    }

    // ============================================
    // Utility Functions
    // ============================================

    /**
     * @notice Send native token to a recipient
     * @param recipient Address to send to
     * @param amount Amount to send
     */
    function sendValue(address payable recipient, uint256 amount) internal {
        (bool success,) = recipient.call{value: amount}("");
        if (!success) revert IStakingVault.StakingVault__TransferFailed();
    }

    /**
     * @notice Require address is not zero
     * @param addr Address to check
     */
    function requireNonZero(address addr) internal pure {
        if (addr == address(0)) revert IStakingVault.StakingVault__ZeroAddress();
    }

    // ============================================
    // Manager Query Helpers
    // ============================================

    /// @notice Get validator stake amount from ValidatorManager
    /// @dev Uses cached ValidatorManager address and weightToValueFactor for gas efficiency
    /// @param validationID The validator ID to query
    /// @return amount The stake amount (0 if validator not found)
    function getValidatorStakeAmountFromManager(bytes32 validationID) internal view returns (uint256 amount) {
        StakingVaultStorageLib.StakingVaultStorage storage $ = StakingVaultStorageLib._getStorage();

        address mgr = $.cachedValidatorManager;
        uint256 wtv = $.cachedWeightToValueFactor;
        if (mgr == address(0) || wtv == 0) return 0;

        (bool success, bytes memory data) = mgr.staticcall(
            abi.encodeWithSelector(StakingVaultStorageLib.SEL_GET_VALIDATOR, validationID)
        );
        if (!success || data.length == 0) return 0;

        // Use abi.decode for proper handling of dynamic bytes in Validator struct
        Validator memory validator = abi.decode(data, (Validator));
        amount = uint256(validator.startingWeight) * wtv;
    }

    /// @notice Get validator start time from ValidatorManager
    /// @dev Uses cached ValidatorManager address for gas efficiency
    /// @param validationID The validator ID to query
    /// @return startTime The validator start time (0 if not found)
    function getValidatorStartTimeFromManager(bytes32 validationID) internal view returns (uint64 startTime) {
        address mgr = StakingVaultStorageLib._getStorage().cachedValidatorManager;
        if (mgr == address(0)) return 0;

        (bool success, bytes memory data) = mgr.staticcall(
            abi.encodeWithSelector(StakingVaultStorageLib.SEL_GET_VALIDATOR, validationID)
        );
        if (!success || data.length == 0) return 0;

        Validator memory validator = abi.decode(data, (Validator));
        return validator.startTime;
    }

    /// @notice Get full delegator info from StakingManager in a single staticcall
    /// @dev Combines status, amount, and startTime queries. Returns success flag
    ///      to distinguish call failure from genuine Unknown(0) status.
    /// @return success True if SM call succeeded (false = skip, DON'T treat as Unknown)
    /// @return status SM delegator status (0=Unknown, 1=PendingAdded, 2=Active, 3=PendingRemoved)
    /// @return amount Delegation stake amount (weight × cachedWeightToValueFactor)
    /// @return startTime Delegation start time (0 if pending)
    function getDelegatorFullInfo(bytes32 delegationID)
        internal view
        returns (bool success, uint8 status, uint256 amount, uint64 startTime)
    {
        StakingVaultStorageLib.StakingVaultStorage storage $ = StakingVaultStorageLib._getStorage();

        uint256 wtv = $.cachedWeightToValueFactor;

        bytes memory data;
        (success, data) = address($.stakingManager).staticcall(
            abi.encodeWithSelector(StakingVaultStorageLib.SEL_GET_DELEGATOR_INFO, delegationID)
        );
        if (!success || data.length < 192) {
            return (false, 0, 0, 0);
        }

        // Delegator struct layout: status(word0), owner(word1), validationID(word2), weight(word3), startTime(word4)
        uint64 weight;
        assembly {
            status := mload(add(data, 32))
            weight := mload(add(data, 128))
            startTime := mload(add(data, 160))
        }
        if (wtv > 0) {
            amount = uint256(weight) * wtv;
        }
    }

    /// @notice Get validator status from ValidatorManager
    /// @dev Status values: 0=Unknown, 1=PendingAdded, 2=Active, 3=PendingRemoved, 4=Completed, 5=Invalidated
    ///      After completeValidatorRemoval, status becomes 4 (Completed) or 5 (Invalidated)
    ///      Validator data (including weight) is preserved even after completion
    /// @param validationID The validation ID to query
    /// @return status The validator status (0 if not found)
    function getValidatorStatusFromManager(bytes32 validationID) internal view returns (uint8 status) {
        address mgr = StakingVaultStorageLib._getStorage().cachedValidatorManager;
        if (mgr == address(0)) return 0;

        (bool success, bytes memory data) = mgr.staticcall(
            abi.encodeWithSelector(StakingVaultStorageLib.SEL_GET_VALIDATOR, validationID)
        );
        if (!success || data.length == 0) return 0;

        Validator memory validator = abi.decode(data, (Validator));
        return uint8(validator.status);
    }
}
