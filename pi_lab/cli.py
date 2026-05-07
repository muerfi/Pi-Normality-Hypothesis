"""Command-line interface for pi_lab."""

import argparse
from pathlib import Path

from pi_lab.digits import generate_pi_digits, load_pi_digits
from pi_lab.search import search_sequence
from pi_lab.statistics import block_frequencies
from pi_lab.visualization import plot_digit_frequencies


def _add_data_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--data",
        type=Path,
        default=None,
        help="Path to a pi digit file. Defaults to data/pi_decimals.txt.",
    )


def generate_command(args: argparse.Namespace) -> int:
    output = generate_pi_digits(args.digits, args.output, overwrite=args.overwrite)
    print(f"Saved {args.digits} pi digits to {output}")
    return 0


def frequency_command(args: argparse.Namespace) -> int:
    pi_digits = load_pi_digits(args.data)
    counts = block_frequencies(pi_digits, block_size=args.block_size)
    print(f"Analyzed {len(pi_digits)} loaded digits with block size {args.block_size}.")
    for block, count in counts.items():
        print(f"{block}\t{count}")

    if args.block_size == 1 and not args.no_plot:
        output = plot_digit_frequencies(pi_digits, args.output)
        print(f"Saved digit-frequency plot to {output}")
    return 0


def search_command(args: argparse.Namespace) -> int:
    pi_digits = load_pi_digits(args.data)
    position = search_sequence(args.sequence, pi_digits)
    if position is None:
        print(f"Sequence '{args.sequence}' was not found in the loaded {len(pi_digits)} digits.")
    else:
        print(f"Sequence '{args.sequence}' found at zero-based position {position}.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m pi_lab",
        description="Finite pi digit generation, search, and frequency tools.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser("generate", help="Generate a local pi digit file.")
    generate_parser.add_argument("--digits", type=int, default=1_000_000, help="Number of digits to write.")
    generate_parser.add_argument("--output", type=Path, default=None, help="Output path for generated digits.")
    generate_parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing output file.")
    generate_parser.set_defaults(func=generate_command)

    frequency_parser = subparsers.add_parser("frequency", help="Count digit or block frequencies.")
    frequency_parser.add_argument("--block-size", type=int, default=1, help="Overlapping block size to count.")
    frequency_parser.add_argument("--output", type=Path, default=None, help="Plot path for block size 1.")
    frequency_parser.add_argument("--no-plot", action="store_true", help="Do not create a plot for block size 1.")
    _add_data_argument(frequency_parser)
    frequency_parser.set_defaults(func=frequency_command)

    search_parser = subparsers.add_parser("search", help="Search for a digit sequence.")
    search_parser.add_argument("--sequence", required=True, help="Digit sequence to search for, e.g. 314159.")
    _add_data_argument(search_parser)
    search_parser.set_defaults(func=search_command)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
