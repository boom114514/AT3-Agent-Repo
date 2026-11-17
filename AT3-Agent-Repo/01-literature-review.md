# Part ① Literature Review — PEFT / LoRA

## Core papers (>=5, 2 from 2024+ top venues)

| ID | Paper | Venue/Year | Role |
|---|---|---|---|
| P1 | LoRA | ICLR 2022 | Base method |
| P2 | AdaLoRA | ICLR 2023 | Rank allocation |
| P3 | QLoRA | NeurIPS 2023 | Quantization + LoRA |
| P4 | LoRA+ | ICML 2024 | Scaling fix (2024) |
| P5 | HydraLoRA | NeurIPS 2024 Oral | Multi-adapter (2024) |
| P6 | Mixture of LoRA Experts | ICLR 2024 | MoE-style (2024) |
| P7 | Variable-Rank LoRA Survey | 2025 | Taxonomy reference |

## Structured table

| Category | Representative | Core idea | Cost / limitation | 2024+ trend |
|---|---|---|---|---|
| Base low-rank | LoRA (P1) | Freeze W0, learn BA, mergeable | Fixed rank/scope | — |
| Rank allocation | AdaLoRA (P2) | Dynamic rank budget | Training complexity | MoE integration |
| Quantized LoRA | QLoRA (P3) | 4-bit base + LoRA | Quantization error | Still practical |
| Scaling fix | LoRA+ (P4) | Different LRs for A/B | Two LR tuning | ICML 2024 |
| Multi-adapter | HydraLoRA (P5), MoLE (P6) | Multiple LoRA experts + routing | Routing overhead | NeurIPS/ICLR 2024 |

## Critical summary

PEFT research has shifted from "can low-rank replace full FT" to "how to allocate rank, combine adapters, and preserve performance on quantized bases". 2024 top-venue work (LoRA+, HydraLoRA, MoLE) shows single fixed-rank LoRA has capacity limits, but multi-adapter methods add routing overhead and training instability. Existing surveys list methods but lack unified small-scale generative ablation — this is the gap Part ② fills.
