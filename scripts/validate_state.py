"""Basic integrity checks for the English Coach state files."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "error-registry.md"

required = [
    ROOT / "SKILL.md",
    ROOT / "AGENT_INSTRUCTIONS.md",
    ROOT / "config.yaml",
    ROOT / "data" / "profile.md",
    REGISTRY,
    ROOT / "data" / "pronunciation.md",
    ROOT / "data" / "vocabulary.md",
    ROOT / "data" / "fluency.md",
    ROOT / "data" / "progress.md",
    ROOT / "data" / "session-index.md",
]

missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    print("Missing required files:")
    for p in missing:
        print(" -", p)
    sys.exit(1)

text = REGISTRY.read_text(encoding="utf-8")
ids = re.findall(r"^###\s+([A-Z][A-Z0-9-]+)\s+—", text, flags=re.MULTILINE)
duplicates = sorted({x for x in ids if ids.count(x) > 1})

if duplicates:
    print("Duplicate canonical error IDs:", ", ".join(duplicates))
    sys.exit(2)

print("State validation passed.")
print(f"Canonical error entries: {len(ids)}")
