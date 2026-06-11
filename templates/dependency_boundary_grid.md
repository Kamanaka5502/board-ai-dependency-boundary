# Dependency Boundary Grid

| Boundary Area | Question | Status | Evidence | Outcome |
|---|---|---:|---|---|
| Memory | Does the dependency retain sensitive or operational memory? | Unknown |  |  |
| Inference | Does output influence decisions that bind consequence? | Unknown |  |  |
| Runtime | Does an agent/runtime execute actions or route workflows? | Unknown |  |  |
| Tools | Can tools mutate systems, records, or access? | Unknown |  |  |
| APIs | Does the dependency call internal or external APIs? | Unknown |  |  |
| Data Retention | Can retained data be deleted, exported, audited, and severed? | Unknown |  |  |
| Jurisdiction | Does processing or retention cross jurisdictional boundaries? | Unknown |  |  |
| Authority | Does approval authority match consequence class? | Unknown |  |  |
| Consequence | What consequence can bind if the dependency acts or fails? | Unknown |  |  |
| Exit Path | Can the organization revoke, isolate, migrate, or override? | Unknown |  |  |
| Audit / Replay | Can the decision and boundary behavior be replayed? | Unknown |  |  |

## Classification

**Green:** bounded, reversible, non-structural, low consequence.  
**Yellow:** emerging load-bearing dependency; narrow, escalate, or revalidate.  
**Red:** structural or high-consequence dependency without sufficient proof; refuse, halt, or board escalation.
