# ⚡ Scoring Methodology

## Purpose

The scoring methodology converts dependency-boundary facts into a repeatable classification.

It is not a generic risk score. It measures whether an AI dependency is admissible as a potential **load-bearing dependency**.

---

## Score Scale

| Score | Meaning |
|---:|---|
| **0** | Absent or unknown |
| **1** | Weak or partial |
| **2** | Documented |
| **3** | Verified |
| **4** | Tested and replayable |

---

## Dimensions

- **Authority**
- **Retention**
- **Jurisdiction**
- **Consequence**
- **Reversibility**
- **Exit**
- **Receipt**
- **Replay**

---

## Classification

| Classification | Meaning |
|---|---|
| 🟢 **Green** | Boundary is documented, verified, and sufficiently replayable |
| 🟡 **Yellow** | Boundary is partially documented and requires narrowing or revalidation |
| 🔴 **Red** | Boundary cannot support structural admission |

---

## Hard Red Triggers

A dependency can be classified **Red** even if some scores are acceptable when a hard boundary failure exists:

- **High consequence without matching authority**
- **Persistent memory without retention control**
- **Regulated workflow without escalation**
- **Critical dependency without exit path**
- **High consequence without receipt**
- **High consequence without replay**

---

## Rule

**The score informs the decision. The hard boundary triggers control admission.**
