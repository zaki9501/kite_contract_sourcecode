#!/usr/bin/env python3
"""
Restructure in_scope_sources into a clean audit-friendly layout:

audit_scope/
├── 1_ValidatorStaking/
│   ├── KiteStakingManager.sol        (impl - main audit target)
│   ├── RewardVault.sol
│   ├── FixedAPRRewardCalculator.sol
│   ├── ValidatorMessages.sol
│   └── _proxies/                     (proxy contracts, lower priority)
├── 2_StakingVault_LST/
│   ├── StakingVault.sol
│   ├── StakingVaultOperations.sol
│   └── _proxies/
├── 3_Tokens/
│   ├── WKITE.sol
│   ├── USDC_e/
│   ├── USDT/
│   └── WETH/
├── 4_AlgebraDEX/
│   ├── AlgebraFactory.sol
│   ├── AlgebraPoolDeployer.sol
│   ├── AlgebraPool.sol
│   ├── SwapRouter.sol
│   ├── NonfungiblePositionManager.sol
│   └── Multicall3.sol
├── 5_KITE_CrossChain/
│   └── Kite.sol                      (OFT token - same on ETH/BSC/Avax)
├── 6_LayerZero/
│   ├── EndpointV2.sol
│   ├── SendUln302.sol
│   ├── ReceiveUln302.sol
│   ├── BlockedMessageLib.sol
│   └── _proxies/
├── 7_LucidBridge/
│   ├── AssetController.sol
│   ├── LockReleaseAssetController.sol
│   └── BaseAssetBridge.sol
├── _dependencies/                    (shared OZ, LayerZero libs, etc.)
└── _metadata/                        (fetch summary, addresses)
"""

import json
import os
import shutil
from pathlib import Path

SRC = Path(__file__).parent / "in_scope_sources"
DST = Path(__file__).parent / "audit_scope"

# Files/folders to skip entirely (not useful for audit)
SKIP_PATTERNS = {
    "metadata.json",
    "immutable-references.json",
    "creator-tx-hash.txt",
    "constructor-args.txt",
    "library-map.json",
}

# Dependency prefixes to move to shared _dependencies
DEP_PREFIXES = (
    "@openzeppelin",
    "@layerzerolabs",
    "solidity-bytes-utils",
    "hardhat",
)


def is_dependency(rel_path: Path) -> bool:
    parts = rel_path.parts
    if not parts:
        return False
    return any(parts[0].startswith(p) for p in DEP_PREFIXES)


def should_skip(name: str) -> bool:
    return name in SKIP_PATTERNS


def copy_file(src: Path, dst: Path):
    # Use Windows extended-length path prefix for long paths
    src_str = str(src.resolve())
    dst_str = str(dst.resolve())
    if os.name == 'nt':
        if not src_str.startswith('\\\\?\\'):
            src_str = '\\\\?\\' + src_str
        if not dst_str.startswith('\\\\?\\'):
            dst_str = '\\\\?\\' + dst_str
    Path(dst_str).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_str, dst_str)


def main():
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)

    # Category mapping: folder prefix -> (section_folder, is_proxy)
    CATEGORIES = {
        # 1. Validator Staking
        "KiteStakingManager_Impl": ("1_ValidatorStaking", False),
        "KiteStakingManager_Proxy": ("1_ValidatorStaking/_proxies", True),
        "RewardVault": ("1_ValidatorStaking", False),
        "FixedAPRRewardCalculator": ("1_ValidatorStaking", False),
        "ValidatorMessages": ("1_ValidatorStaking", False),
        "Staking_ProxyAdmin": ("1_ValidatorStaking/_proxies", True),
        # 2. Staking Vault (LST)
        "StakingVault_Impl": ("2_StakingVault_LST", False),
        "StakingVault_Proxy": ("2_StakingVault_LST/_proxies", True),
        "StakingVaultOperations_Impl": ("2_StakingVault_LST", False),
        # 3. Tokens
        "WKITE": ("3_Tokens", False),
        "USDC_e": ("3_Tokens/USDC_e", False),
        "USDT__": ("3_Tokens/USDT", False),
        "WETH__": ("3_Tokens/WETH", False),
        # 4. Algebra DEX
        "AlgebraFactory": ("4_AlgebraDEX", False),
        "AlgebraPoolDeployer": ("4_AlgebraDEX", False),
        "SwapRouter": ("4_AlgebraDEX", False),
        "NonfungiblePositionManager": ("4_AlgebraDEX", False),
        "Multicall3": ("4_AlgebraDEX", False),
        # 5. KITE Cross-Chain (only need one copy - same bytecode)
        "KITE_Ethereum": ("5_KITE_CrossChain", False),
        "KITE_BSC": (None, True),  # Skip - duplicate
        "KITE_Avalanche": (None, True),  # Skip - duplicate
        # 6. LayerZero
        "LayerZero_EndpointV2": ("6_LayerZero", False),
        "LayerZero_SendUln302": ("6_LayerZero", False),
        "LayerZero_ReceiveUln302": ("6_LayerZero", False),
        "LayerZero_LZExecutor": ("6_LayerZero/_proxies", True),
        "LayerZero_BlockedMessageLibrary": ("6_LayerZero", False),
        # 7. Lucid Bridge (Kite versions only - same as Avalanche/Celo)
        "Lucid_USDC_Controller__": ("7_LucidBridge", False),
        "Lucid_WETH_Controller__": ("7_LucidBridge", False),
        "Lucid_USDT_Controller__": ("7_LucidBridge", False),
        "Lucid_USDC_Controller_Avalanche": (None, True),  # Skip - duplicate
        "Lucid_WETH_Controller_Avalanche": (None, True),  # Skip - duplicate
        "Lucid_USDT_Controller_Celo": (None, True),  # Skip - duplicate
    }

    deps_seen: set[str] = set()
    deps_dst = DST / "_dependencies"
    meta_dst = DST / "_metadata"
    meta_dst.mkdir(parents=True, exist_ok=True)

    # Copy fetch summary to metadata
    summary_src = SRC / "_fetch_summary.json"
    if summary_src.exists():
        shutil.copy2(summary_src, meta_dst / "fetch_summary.json")

    # Create address reference
    addresses: dict[str, str] = {}

    for folder in sorted(SRC.iterdir()):
        if not folder.is_dir():
            continue

        folder_name = folder.name
        # Extract address from folder name
        if "__0x" in folder_name:
            label, addr = folder_name.rsplit("__", 1)
        else:
            label, addr = folder_name, ""

        # Find matching category
        cat_folder = None
        is_skip = False
        for prefix, (dest, skip_flag) in CATEGORIES.items():
            if label.startswith(prefix) or label == prefix.rstrip("_"):
                cat_folder = dest
                is_skip = skip_flag if dest is None else False
                break

        if is_skip or cat_folder is None:
            print(f"SKIP: {folder_name}")
            continue

        if addr:
            addresses[label] = addr

        target_base = DST / cat_folder

        # Walk files in this contract folder
        for root, dirs, files in os.walk(folder):
            root_path = Path(root)
            rel_root = root_path.relative_to(folder)

            for fname in files:
                if should_skip(fname):
                    continue

                src_file = root_path / fname
                rel_file = rel_root / fname

                if is_dependency(rel_file):
                    # Move to shared dependencies (dedupe)
                    dep_key = str(rel_file)
                    if dep_key not in deps_seen:
                        deps_seen.add(dep_key)
                        copy_file(src_file, deps_dst / rel_file)
                else:
                    # Copy to category folder
                    # Flatten simple single-file contracts
                    if rel_root == Path(".") or str(rel_root) in ("contracts", "src"):
                        dst_file = target_base / fname
                    else:
                        dst_file = target_base / rel_file
                    copy_file(src_file, dst_file)

    # Write address reference
    (meta_dst / "addresses.json").write_text(
        json.dumps(addresses, indent=2), encoding="utf-8"
    )

    # Create README for audit scope
    readme = """# Kite AI Bug Bounty - Audit Scope

## Structure

| Folder | Description | Priority |
|--------|-------------|----------|
| `1_ValidatorStaking/` | Staking manager, reward vault, APR calculator | HIGH |
| `2_StakingVault_LST/` | Liquid staking vault (LST) | HIGH |
| `3_Tokens/` | WKITE, USDC.e, USDT, WETH on Kite | MEDIUM |
| `4_AlgebraDEX/` | Algebra concentrated liquidity DEX | MEDIUM |
| `5_KITE_CrossChain/` | KITE OFT token (ETH/BSC/Avax) | MEDIUM |
| `6_LayerZero/` | LayerZero bridge contracts | MEDIUM |
| `7_LucidBridge/` | Lucid asset controllers | MEDIUM |
| `_proxies/` subfolders | Proxy contracts (OZ patterns) | LOW |
| `_dependencies/` | Shared OpenZeppelin / LZ libs | REFERENCE ONLY |
| `_metadata/` | Addresses, fetch summary | INFO |

## Missing Source (Not Verified)

- `0x6788f52439ACA6BFF597d3eeC2DC9a44B8FEE842` - LZ Dead DVN (no verified source on Kitescan)

## Quick Start

1. Focus on folders 1-2 first (validator staking, LST vault) - core Kite logic
2. Then review 4 (Algebra DEX) and 7 (Lucid) for integration risks
3. Cross-chain token (5) and LayerZero (6) are mostly standard LZ patterns
4. `_proxies/` are standard OZ upgradeable patterns - lower priority
5. `_dependencies/` is reference only - don't audit OZ/LZ library code

## Contract Addresses

See `_metadata/addresses.json` for all deployed addresses.
"""
    (DST / "README.md").write_text(readme, encoding="utf-8")

    # Print summary
    print(f"\n[OK] Created audit_scope/ with structured layout")
    print(f"  - Primary contracts organized into 7 sections")
    print(f"  - Dependencies deduplicated to _dependencies/")
    print(f"  - Metadata in _metadata/")
    print(f"\nFile counts:")
    for section in sorted(DST.iterdir()):
        if section.is_dir():
            count = sum(1 for _ in section.rglob("*.sol"))
            print(f"  {section.name}: {count} .sol files")


if __name__ == "__main__":
    main()
