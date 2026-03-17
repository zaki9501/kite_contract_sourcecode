# Kite AI Bug Bounty
### KiteAI

Powering AI agents with an EVM‑compatible payment chain for autonomous, onchain transactions.

**$10,000 in USDC MAX BOUNTY**

---

## **KiteAI Bug Bounty Details**

[**Read our guidelines for more details**](https://docs.code4rena.com/bounties)

Submit findings [**using the C4 form**](https://code4rena.com/bounties/submit)

This is a managed bug bounty program. All triage, severity assessment, and award recommendations are performed by independent Code4rena judges, according to the standard C4 judging and bounty criteria.

Smart Contracts:

| **Risk score** | **Payout (USDC)** |
| --- | --- |
| Critical | Up to **$10,000** |
| High | Up to **$2,000** |

Websites and Apps:

| **Risk score** | **Payout (USDC)** |
| --- | --- |
| Critical | Up to **$10,000** |
| High | Up to **$2,000** |

**Payment terms**

- Payouts are denominated in USD and paid in USDC.
- Bounty payouts will be processed after a 30‑day waiting period following the public deployment and announcement of a fix. This applies to all severity levels.

**KYC required for payout:** If your bounty submission meets the criteria for a reward, you must complete [Certification (ID verification)](https://docs.code4rena.com/roles/certification-id-verification)
---

## **Quick Links**

[**Judging for C4 Bug Bounties**](https://docs.code4rena.com/awarding/judging-criteria/bounty-judging)

[**Criteria for C4 Bug Bounties**](https://docs.code4rena.com/awarding/judging-criteria/bounty-criteria)

---

## **Background on KiteAI**

Kite is the first AI payment blockchain, an EVM‑compatible Layer 1 built specifically for the AI agent economy. It provides cryptographic identity, programmable payment flows, and support for stablecoins and the KITE token so autonomous agents can authenticate and transact onchain.

This bug bounty program is focused on KiteAI’s smart contracts and production web properties, with a focus on preventing:

- Loss of protocol or user funds
- Smart contract vulnerabilities impacting the KITE token or payment flows
- Denial of service issues for core protocol contracts
- Critical infrastructure vulnerabilities on gokite.ai

---

## **Further Technical Resources and Links**

Kite Docs: [**https://docs.gokite.ai**](https://docs.gokite.ai/)

Kite Smart Contracts List: [**https://docs.gokite.ai/kite-chain/3-developing/smart-contracts-list**](https://docs.gokite.ai/kite-chain/3-developing/smart-contracts-list)

Kite Website: [**https://gokite.ai**](https://gokite.ai/)

Twitter: [**https://twitter.com/GoKiteAI**](https://twitter.com/GoKiteAI)

---

## **Scope and Severity Criteria**

The bounty covers vulnerabilities in the in‑scope assets listed below, evaluated according to the standard Code4rena bounty criteria:

- [**Judging for C4 Bug Bounties**](https://docs.code4rena.com/awarding/judging-criteria/bounty-judging)
- [**Criteria for C4 Bug Bounties**](https://docs.code4rena.com/awarding/judging-criteria/bounty-criteria)

Only impacts that meet those criteria and affect the assets in the “Smart contracts in scope” and “Websites and apps in scope” sections will be eligible for rewards. All other impacts are considered out of scope for this program.

KiteAI and the independent judges will determine final severity and payout amounts.

---

## **Smart Contracts in Scope**

Rewards for smart contract vulnerabilities are for issues in the following contracts only.

## **Ethereum**

- KITE token contract
    - `0x904567252D8F48555b7447c67dCA23F0372E16be` (KITE ERC‑20 token)

## **Kite Mainnet**

The following Kite Mainnet contracts are in scope. Names and roles are to be confirmed by the KiteAI team.

- `0xd26850d11e8412fC6035750BE6A871dff9091FAe`
- `0x065cA4309a5abc9F1cC2d8fA00634BC948C25C6b`
- `0x7d627b0F5Ec62155db013B8E7d1Ca9bA53218E82`
- `0x171eefa30E88f9bca456CEf49c5Df093A516C7c2`
- `0xcc788DC0486CD2BaacFf287eea1902cc09FbA570`

Source code for these contracts is available in KiteAI’s GitHub organization:

[**https://github.com/gokite-ai**](https://github.com/gokite-ai)

Payouts are handled by the KiteAI team and denominated in USDC. Payouts will be made in USDC (on Ethereum or Kite Mainnet, as determined by KiteAI).

---

## **Websites and Apps in Scope**

The following web assets are in scope for this bug bounty program:

- All production properties under `.gokite.ai`
    - Including, for example, the main application at [**https://gokite.ai**](https://gokite.ai/) and any hosted dashboards or configuration interfaces

Staging, test, and non‑production environments are not in scope unless explicitly added by KiteAI.

---

## **Out of Scope**

The following are out of scope for this program, in addition to anything excluded by Code4rena’s standard bounty criteria:

- Contracts and applications not listed in the “Smart contracts in scope” or “Websites and apps in scope” sections
- Vulnerabilities previously identified in public audits or security reports for KiteAI
- Purely informational findings without demonstrable security impact, as per C4 criteria
- Any issues already known to KiteAI at the time of submission

KiteAI may maintain a public list of known issues and closed reports. Any item on that list is automatically out of scope for bounty rewards.

---

## **Previous Audits**

Issues reported in past audits are out of scope and not eligible for rewards.

- Halborn – GoKite Contracts Audit (2025)
- Halborn – Kite Core Contracts Audit (2025)

KiteAI may add additional audits here over time.

---

## **Specific Types of Issues**

The following types of issues are excluded from rewards for this bug bounty program unless they directly lead to one of the accepted impact types in the Code4rena criteria:

- Attacks that the reporter has already exploited for profit or used for personal gain
- Attacks requiring access to compromised private keys or leaked credentials
- Attacks that require full control of a trusted admin or governance key without an underlying code vulnerability
- Generic best‑practice hardening suggestions without concrete exploitability
- Issues only affecting non‑production environments

For full details on in‑scope versus out‑of‑scope impact categories, see:

- [**Criteria for C4 Bug Bounties**](https://docs.code4rena.com/awarding/judging-criteria/bounty-criteria)

---

## **Prohibited Activities**

The following activities are strictly prohibited under this bug bounty program:

- Any testing directly on Ethereum or Kite Mainnet that risks real user funds
- Any testing involving third‑party contracts or oracles outside of the listed in‑scope assets
- Phishing or social engineering attacks against KiteAI team members or users
- Attacks against, or use of, third‑party infrastructure or services (for example, cloud providers, analytics, or email providers)
- Denial of service attacks against KiteAI infrastructure
- Automated scanning or fuzzing that generates excessive traffic or degrades service for real users
- Public disclosure of an unpatched vulnerability before KiteAI and Code4rena have confirmed remediation

---

## **Additional Context**

Current and past employees or contractors of KiteAI and their family members are not eligible for rewards from this bug bounty program.
