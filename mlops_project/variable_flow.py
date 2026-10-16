from __future__ import annotations

import argparse
from pathlib import Path


def update_value(current_value: int, output_file: str) -> int:
    """Increment the value and persist it for the next workflow step."""
    next_value = current_value + 1

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(next_value), encoding="utf-8")

    print(f"Received value: {current_value}")
    print(f"Updated value saved: {next_value}")
    print(f"Saved to: {output_path}")
    return next_value


def main() -> None:
    parser = argparse.ArgumentParser(description="Pass and update a variable across CI steps.")
    parser.add_argument("--value", type=int, required=True, help="Current value passed from the workflow.")
    parser.add_argument(
        "--output-file",
        default="artifacts/updated_value.txt",
        help="File where the next value will be saved.",
    )
    args = parser.parse_args()

    update_value(args.value, args.output_file)


if __name__ == "__main__":
    main()
