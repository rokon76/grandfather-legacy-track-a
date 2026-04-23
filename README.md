## ⚖️ Validator & Auditing Logic
This repository serves as the **Owner of Truth** for the subnet. It utilizes a multi-stage audit process:

1. **Physical Consistency:** Uses the Casimir Pressure equation to verify if the reported `loading_time` is possible given the `lattice_gap`.
2. **Scoring:** Calculates the percentage improvement over the 2.2s baseline.
3. **Weight Mapping:** Translates scores into network weights for reward distribution.

### 🚫 Anti-Cheat Requirements
Submissions are rejected if:
- Loading time is >= 2.2s.
- The claim violates the **Pressure-Time Constraint** (Sub-2.1s requires > 500k ATM).
## 🛠️ Local Setup & Telegram Configuration

To protect network security, private API keys and credentials are not stored in this repository. To enable real-time Telegram alerts for your validator node, follow these steps:

### 1. Create your Environment File
Create a file named `.env` in your root directory (this is already ignored by `.gitignore`) and add your credentials:

```text
TG_TOKEN=your_bot_token_here
TG_CHAT_ID=your_chat_id_here

## 📊 Network Statistics
- **Current World Record:** 🏆 `2.05s` (Miner_Alpha_01)
- **Verified Lattice Gap:** `0.3nm`
- **Network Difficulty:** Sub-2.1s (Requires > 500k ATM)
