## ⚖️ Validator & Auditing Logic
This repository serves as the **Owner of Truth** for the subnet. It utilizes a multi-stage audit process:

1. **Physical Consistency:** Uses the Casimir Pressure equation to verify if the reported `loading_time` is possible given the `lattice_gap`.
2. **Scoring:** Calculates the percentage improvement over the 2.2s baseline.
3. **Weight Mapping:** Translates scores into network weights for reward distribution.

### 🚫 Anti-Cheat Requirements
Submissions are rejected if:
- Loading time is >= 2.2s.
- The claim violates the **Pressure-Time Constraint** (Sub-2.1s requires > 500k ATM).
