import json
from pathlib import Path

ROOT = Path(__file__).parent

def validate():
    errors = []
    brief = ROOT / "final-brief.md"
    if not brief.exists():
        return {"ok": False, "errors": ["final-brief.md not found"]}

    text = brief.read_text(encoding="utf-8")
    required = ["P1", "P4", "P5"]
    for c in required:
        if f"[{c}]" not in text:
            errors.append(f"missing citation [{c}]")

    sources = {p.stem.split("_")[0]: p.read_text(encoding="utf-8")
               for p in (ROOT / "sources").glob("*.md")}
    for c in required:
        if c not in sources:
            errors.append(f"source {c} not found")

    return {"ok": len(errors) == 0, "errors": errors}

if __name__ == "__main__":
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
