# Signal Semaphore

> Operating circular 04: constrained meaning, shared state, no hidden referee.

## Line notice

Signal Semaphore is a cooperative GenLayer game. A station master freezes a target phrase, a category, permitted signal types, forbidden terms, a round limit, and a designated signaler. The signaler must guide another wallet without naming, spelling, translating, encoding, or trivially leaking the target.

## Cabin diagram

| Apparatus | Contract authority |
| --- | --- |
| Line plate | Immutable game configuration |
| Red lamp | `SIGNALING` or blocked clue |
| Semaphore arm | Validator-reviewed transmission |
| Green lamp | Exact semantic match |
| Bell register | Canonical clue and answer history |

## Block rules

`transmit` uses validator consensus to test leakage, forbidden language, category fit, and indirect usefulness. `answer` asks a separate consensus question about semantic identity. Code alone advances rounds, counts faults, and selects `LINE_CLEAR`, `MISSED`, or `LINE_BLOCKED`.

## Crew sequence

1. Connect the station master wallet and open a game.
2. The designated signaler pulls one permitted signal.
3. A different wallet rings an answer.
4. Read the finalized block state and bell ticket from StudioNet.

## Commissioning

```bash
cd frontend
npm install
npm run typecheck
npm run build
```

Contract source is `contracts/contract.py`. The pinned GenVM runner is declared on its first line. Surface tests run with `pytest -q` from the repository root.

## Bell register

The application reads and writes the Intelligent Contract directly through `genlayer-js`. There is no application server, simulated verdict, deposit, escrow, or administrative shortcut.
