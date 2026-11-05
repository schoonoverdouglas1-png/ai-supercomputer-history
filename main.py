"""ai-supercomputer-history starter.

Prints the Google AI lineage from timeline.json.
No API key needed. Standard library only.
Recreated by Ember, Nov 5, 2026, from Meta AI's description as brought by Douglas.
"""
import json
from pathlib import Path


def main():
    data = json.loads((Path(__file__).parent / "timeline.json").read_text())
    print(data["title"])
    print("=" * len(data["title"]))
    for event in data["events"]:
        print(f"{event['year']}: {event['name']} — {event['note']}")
    print()
    print("Open source / open weights:", ", ".join(data["open_source"]))
    print("API-only:", ", ".join(data["api_only"]))
    print()
    print("Supercomputers:")
    for machine in data["supercomputers"]:
        print(f"  - {machine['name']} ({machine['type']})")


if __name__ == "__main__":
    main()
