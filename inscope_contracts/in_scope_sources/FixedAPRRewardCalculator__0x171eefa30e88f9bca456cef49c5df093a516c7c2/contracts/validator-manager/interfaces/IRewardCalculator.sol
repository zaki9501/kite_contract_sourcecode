// (c) 2024, Ava Labs, Inc. All rights reserved.
// See the file LICENSE for licensing terms.

// SPDX-License-Identifier: LicenseRef-Ecosystem

pragma solidity 0.8.25;

/**
 * @notice Interface for Validation and Delegation reward calculators
 */
interface IRewardCalculator {
    /**
     * @notice Calculate incremental reward for a staker during an active staking period.
     * This is used when validators/delegators claim rewards without ending their stake.
     * @param stakeAmount The amount of tokens staked
     * @param lastClaimTime The timestamp of the last reward claim (or staking start if first claim)
     * @param currentTime The current timestamp
     * @param lastClaimUptimeSeconds The uptime seconds at the last claim
     * @param currentUptimeSeconds The current uptime seconds
     * @param validatorStartTime The time the validator started validating
     * @return reward The calculated reward amount
     */
    function calculateIncrementalReward(
        uint256 stakeAmount,
        uint64 lastClaimTime,
        uint64 currentTime,
        uint64 lastClaimUptimeSeconds,
        uint64 currentUptimeSeconds,
        uint64 validatorStartTime
    ) external view returns (uint256 reward);
}
