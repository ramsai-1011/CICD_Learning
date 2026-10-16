from __future__ import annotations

import argparse
from pathlib import Path


def validate_pair(a: int, b: int) -> tuple[int, int]:
    """Ensure a and b form a valid 100% pair for promotion checks."""
    total = a + b
    if total != 100:
        raise ValueError(
            f"Invalid inputs: a={a} and b={b} must sum to 100. Got {total}."
        )
    return a, b


def write_summary(a: int, b: int, output_file: str | None = None) -> None:
    """Persist the validated values for downstream workflow steps."""
    output_path = Path(output_file) if output_file else Path("artifacts/validated_pair.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"a={a}\nb={b}\n total={a + b}\n", encoding="utf-8")

    print(f"Validated pair: a={a}, b={b}, total={a + b}")
    print(f"Saved summary to: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate two values that must sum to 100.")
    parser.add_argument("--a", type=int, default=100, help="First input value. Default: 100")
    parser.add_argument("--b", type=int, default=0, help="Second input value. Default: 0")
    parser.add_argument(
        "--output-file",
        default="artifacts/validated_pair.txt",
        help="Optional file to store the validated pair.",
    )
    args = parser.parse_args()

    a, b = validate_pair(args.a, args.b)
    write_summary(a, b, args.output_file)


if __name__ == "__main__":
    main()
