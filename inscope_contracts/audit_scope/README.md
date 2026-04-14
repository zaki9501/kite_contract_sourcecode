# Kite AI Bug Bounty - Audit Scope

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
