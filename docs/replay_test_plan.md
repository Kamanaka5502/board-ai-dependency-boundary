# 🔁 Replay Test Plan

## Purpose

Replay proves whether the dependency boundary decision holds under repeated inspection.

A valid replay means:

- The same dependency facts produce the same decision.
- Changed facts produce a changed decision.
- Expired authority triggers revalidation.
- Expanded scope triggers escalation.
- Failed retention boundary triggers refusal or halt.
- Revoked access prevents continuation.
- Protected consequence does not bind when the boundary fails.

---

## Replay Questions

| Test | Expected Boundary Behavior |
|---|---|
| Same facts submitted twice | Same decision outcome |
| Authority removed | Revalidate / Escalate / Refuse |
| Retention changes | Revalidate / Narrow / Halt |
| Cross-border storage introduced | Escalate / Narrow / Refuse |
| Agent autonomy added | Escalate / Narrow / Halt |
| Financial movement added | Escalate / Refuse unless authority is proven |
| Revocation requested | Dependency cannot continue if access is revoked |
| Exit path fails | Red classification or Halt |

---

## Buyer Rule

**No replay, no confidence that the boundary held.**
