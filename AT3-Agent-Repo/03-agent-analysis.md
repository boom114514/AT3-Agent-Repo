# Part ③ Agent Task Analysis (two pages)

## Completion status
Both `max_steps=3` and `max_steps=6` pass the validator. The 6-step run contains 3 noop steps, showing that only the first 3 steps are effective.

## Tool calls and citation evidence
`search_sources("low-rank") -> read_source("P1") -> write_brief(...)`. Citations `[P1]`, `[P4]`, `[P5]` are grounded in `sources/P1_lora.md`, `P4_lora_plus.md`, `P5_hydra_lora.md`.

## Most error-prone step
`write_brief` must cover all three required citations; otherwise the validator reports `missing citation`.

## Controlled comparison
| Condition | Validator pass? | Effective tool calls | Notes |
|---|---|---|---|
| max_steps=3 | yes | 3 | write_brief lands on step 3 |
| max_steps=6 | yes | 3 + 3 noop | exposes wasted steps |

## Limitation
This fixture uses a rule-based offline policy, not a real LLM. It validates the contract / tool schema / trajectory / validator chain, not model reasoning.
