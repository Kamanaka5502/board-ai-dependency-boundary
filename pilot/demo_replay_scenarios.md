# 🔁 Demo Replay Scenarios

## Purpose

Replay verifies that the dependency decision is not a one-time opinion. It proves the boundary decision can be reconstructed and that changed facts trigger changed outcomes.

---

## Replay Tests

| Scenario | Changed Fact | Expected Outcome |
|---|---|---|
| **Same facts replayed** | No change | Same Yellow-to-Red classification |
| **Memory removed** | No persistent memory | Risk may reduce to Yellow |
| **API access narrowed** | No workflow mutation | Narrow may hold without Halt |
| **Board authority confirmed** | Executive approval added | Escalation may resolve if other boundaries hold |
| **Vendor moves processing region** | Jurisdiction changes | Revalidate / Escalate |
| **Tool permissions expand** | More system access | Escalate / Halt |
| **Retention cannot be deleted** | Memory severance fails | Refuse / Halt |
| **Exit path fails** | No fallback continuity | Red classification |

---

## Replay Rule

**No replay, no dependency confidence.**

A dependency that cannot be replayed cannot be trusted as board-assured.
