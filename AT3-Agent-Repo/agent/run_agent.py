import json, os
from pathlib import Path

ROOT = Path(__file__).parent
MAX_STEPS = int(os.environ.get("MAX_STEPS", "3"))

def search_sources(query):
    hits = []
    for p in (ROOT / "sources").glob("*.md"):
        if query.lower() in p.read_text(encoding="utf-8").lower():
            hits.append(p.stem.split("_")[0])
    return hits

def read_source(source_id):
    files = list((ROOT / "sources").glob(f"{source_id}_*.md"))
    return files[0].read_text(encoding="utf-8") if files else "NOT_FOUND"

def write_brief(content):
    (ROOT / "final-brief.md").write_text(content, encoding="utf-8")
    return "written"

steps = []
for i in range(MAX_STEPS):
    if i == 0:
        obs = search_sources("low-rank")
        steps.append({"step": i, "tool": "search_sources", "args": {"query": "low-rank"}, "obs": obs})
    elif i == 1:
        steps.append({"step": i, "tool": "read_source", "args": {"source_id": "P1"}, "obs": read_source("P1")[:120]})
    elif i == 2:
        write_brief("# Brief\n\nLoRA [P1] uses low-rank updates. LoRA+ [P4] fixes scaling. HydraLoRA [P5] uses multi-adapter.\n")
        steps.append({"step": i, "tool": "write_brief", "args": {"content": "..."}, "obs": "written"})
    else:
        steps.append({"step": i, "tool": "noop", "obs": "max_steps reached"})

with open(ROOT / "trajectory.jsonl", "w", encoding="utf-8") as f:
    for s in steps:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

with open(ROOT / "tool-results.jsonl", "w", encoding="utf-8") as f:
    for s in steps:
        if "obs" in s:
            f.write(json.dumps({"step": s["step"], "tool": s["tool"], "result": s["obs"]}, ensure_ascii=False) + "\n")

print("Agent run complete.")
