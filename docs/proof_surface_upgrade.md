# Proof Surface Upgrade

## Status

The public repository now supports a stronger customer-facing proof surface.

This is still a bounded sandbox pilot. It is not the protected Elyria Systems substrate and it is not production enforcement.

---

## Added Proof Capabilities

| Capability | Public Sandbox Behavior |
|---|---|
| Deterministic replay | Same payload produces the same decision and normalized receipt fields |
| Receipt digest | Review + decision are canonicalized and hashed with SHA-256 |
| Changed-condition replay delta | Changed facts can move a dependency into revalidation |
| No-effect behavior | Non-admitted dependencies receive no admit token and no proceed authorization |
| Replay endpoints | `/sandbox/replay` and `/sandbox/replay-delta` expose the replay proof surface |

---

## Receipt Integrity

The public sandbox creates a `receipt_digest` by canonicalizing the submitted review and the resulting decision, then computing a SHA-256 digest.

The digest is not represented as a legal signature, regulatory certification, or production audit seal. It is a sandbox proof artifact showing receipt integrity behavior.

---

## Replay Equality

Replay equality is measured by comparing:

- decision classification
- decision outcome
- decision reason
- normalized receipt fields
- receipt digest

Timestamp-derived fields are excluded from normalized replay comparison.

---

## Changed-Condition Delta

The replay delta surface compares a before payload and after payload.

A dependency that previously admitted can move to revalidation when `conditions_changed` becomes true.

This demonstrates that prior approval is not treated as permanent authority when material facts change.

---

## No-Effect Rule

A dependency receives a proceed authorization only when:

```text
classification == green
outcome == admit
```

All other states receive:

```text
admit_token = null
proceed_authorization = false
```

This demonstrates no-effect behavior for red, yellow, halt, escalate, narrow, refuse, and revalidate conditions.

---

## Buyer Interpretation

This raises the public artifact from a runnable governance demo to a bounded proof-surface sandbox.

It now shows not only a decision, but whether that decision can be replayed, whether the receipt has integrity, whether changed conditions alter standing, and whether inadmissible dependencies are denied proceed authorization.

---

## Boundary

The public sandbox proves the exposed review surface only.

It does not expose:

- protected substrate
- private kernel
- unpublished math
- production enforcement architecture
- internal research corpus
- customer confidential data
- operational secrets
