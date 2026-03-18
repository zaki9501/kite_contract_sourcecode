# Kite AI Bug Bounty
- [Read our guidelines for more details](https://docs.code4rena.com/bounties)
- Submit findings [using the C4 form](https://code4rena.com/bounties/kite-ai/submit)

**Smart Contracts:**

| Risk score | Payout |
| --- | --- |
| Critical | Up to $10,000 in USDC |
| High | Up to $2,000 in USDC |

**Websites and Apps:**

| Risk score | Payout |
| --- | --- |
| Critical | Up to $10,000 in USDC |
| High | Up to $2,000 in USDC |

**Payment terms:**
- Bounty payouts will be processed after a 30‑day waiting period following the public deployment and announcement of a fix. This applies to all severity levels.
- **KYC required for payout:** If your bounty submission meets the criteria for a reward, you must complete [Certification (ID verification)](https://docs.code4rena.com/roles/certification-id-verification)

## Background on Kite AI

[⚡️ Project: Please review/update the short overview of the project below:]

Kite AI is the first AI payment blockchain, an EVM‑compatible Layer 1 built specifically for the AI agent economy. It provides cryptographic identity, programmable payment flows, and support for stablecoins and the KITE token so autonomous agents can authenticate and transact onchain.

### How Does It Work?
[⚡️ Project: Optional: add a high-level technical overview of the project here:]

This bug bounty program is focused on KiteAI’s smart contracts and production web properties, with a focus on preventing:
- Loss of protocol or user funds
- Smart contract vulnerabilities impacting the KITE token or payment flows
- Denial of service issues for core protocol contracts
- Critical infrastructure vulnerabilities on gokite.ai

## Further Technical Resources and Links

- Kite AI Docs: https://docs.gokite.ai/
- Kite AI Smart Contracts List: https://docs.gokite.ai/kite-chain/3-developing/smart-contracts-list
- Kite AI Website: https://gokite.ai/
- X: https://x.com/GoKiteAI

## Scope and Severity Criteria

[⚡️ Project: Please insert any valid information around scope and severity criterias here]

## Smart Contracts in Scope

[⚡️ Project: Please fill any additional Source and scoping information that you deam necessary into the tables below:]

Source: https://github.com/gokite-ai

### Ethereum

| Name | Mainnet address |
| ----- | ----- |
| KITE token contract | `0x904567252D8F48555b7447c67dCA23F0372E16be` (KITE ERC‑20 token) |

### Kite Mainnet

| Name | Mainnet address |
| ----- | ----- |
| - | `0xd26850d11e8412fC6035750BE6A871dff9091FAe` |
| - | `0x065cA4309a5abc9F1cC2d8fA00634BC948C25C6b` |
| - | `0x7d627b0F5Ec62155db013B8E7d1Ca9bA53218E82` |
| - | `0x171eefa30E88f9bca456CEf49c5Df093A516C7c2` |
| - | `0xcc788DC0486CD2BaacFf287eea1902cc09FbA570` |

## Websites and Apps in Scope

- All production properties under [.gokite.ai](https://gokite.ai/)
    - Including, for example, the main application and any hosted dashboards or configuration interfaces.

## Out of Scope

### Known Issues

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. Every issue opened in the repo, closed PRs, previous contests and audits are out of scope.

All issues submitted by wardens to the Kite AI bounty will be added to [this repo](https://github.com/code-423n4/Kite-AI-bug-bounty/issues?q=is%3Aissue%20state%3Aclosed) once they have been reviewed by the sponsors. These are considered known issues and are out-of-scope for bounty rewards.

The following are out of scope for this program, in addition to anything excluded by Code4rena’s standard bounty criteria:
- Contracts and applications not listed in the “Smart contracts in Scope” or “Websites and apps in Scope” sections.
- Staging, test, and non‑production environments at [.gokite.ai](https://gokite.ai/) are not in scope, unless explicitly added by Kite AI.
- Purely informational findings without demonstrable security impact, as per C4 criteria.

## Previous Audits

Any previously reported vulnerabilities mentioned in past audit reports are not eligible for a reward.
- Halborn – [GoKite Contracts Audit (2025)](https://www.halborn.com/audits/kite/gokite-contracts-633ec7)
- Halborn – [Kite Core Contracts Audit (2025)](https://www.halborn.com/audits/kite/kite-031103)
- Halborn - [Kite Staking & Rewards Audit (2026)](https://www.halborn.com/audits/kite/staking--rewards-contracts-2a1577)

Kite AI may add additional audits here over time.

## Specific Types of Issues

[⚡️Project: Please add any other specific types of issues that should be considered out-of-scope.]

The following types of issues are excluded from rewards for this bug bounty program unless they directly lead to one of the accepted impact types in the Code4rena criteria:

- Attacks that the reporter has already exploited for profit or used for personal gain.
- Attacks requiring access to compromised private keys or leaked credentials.
- Attacks that require full control of a trusted admin or governance key without an underlying code vulnerability.
- Generic best‑practice hardening suggestions without concrete exploitability.
- Issues only affecting non‑production environments.

For full details on in‑scope versus out‑of‑scope severity categories, see:
- [**Severity Classifications for C4 Bug Bounties**](https://docs.code4rena.com/bounties/bounty-criteria)

## Prohibited Activities

The following activities are strictly prohibited under this bug bounty program:
- Any testing directly on Ethereum or Kite AI Mainnet that risks real user funds.
- Any testing involving third‑party contracts or oracles outside of the listed in‑scope assets.
- Phishing or social engineering attacks against KiteAI team members or users.
- Attacks against, or use of, third‑party infrastructure or services (for example, cloud providers, analytics, or email providers).
- Denial of service attacks against KiteAI infrastructure.
- Automated scanning or fuzzing that generates excessive traffic or degrades service for real users.
- Public disclosure of an unpatched vulnerability before KiteAI and Code4rena have confirmed remediation.

## Additional Context

### Trusted Roles
[⚡️ Project: Please explain your protocol's trusted roles.]

### Miscellaneous

Employees of Kite AI and their family members are ineligible for bounties.

Reward amounts may be displayed using a dollar sign for simplicity, but the underlying valuation is based on a USD-pegged digital asset such as USDC. Because the displayed figure reflects a USD reference value rather than a fiat currency payment, the final amount delivered in the corresponding token may differ slightly at the time of payout.
