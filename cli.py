"""
Command Line Interface (CLI) for the Brainetry programming language.
"""

import argparse
import sys

from brainetry import E

def btry2bf(code):
    """Translate a brainetry program to brainfuck."""

    result = ""
    for line in code.split("\n"):
        n = len([*filter(bool, line.split(" "))])
        if n > 9:
            continue
        result += "«»><+-,.[]"[n]
    return result

def bf2btry(code):
    """Translate a brainfuck program to brainetry."""

    from lorem import lorem

    while "\n" in lorem:
        lorem = lorem.replace("\n", "")
    lorem = lorem.split(" ")

    result = ""
    source = lorem[::]
    ops = "«»><+-,.[]"
    ops_is = []
    for c in code:
        if c == "\n":
            result += c
        if c in ops:
            i = ops.index(c)
            ops_is.append(i)
            if i > len(source):
                source += lorem[::]
            new = " ".join(source[:i])
            source = source[i:]
            result += new + "\n"

    return ops_is, result

def golf(inp):
    """Golf a Brainetry program to the maximum."""

    r = ""
    for line in inp.split("\n"):
        ran = range(len([*filter(bool, line.split(" "))]))
        ran = ["abcdefghijklm"[i] for i in ran]
        r += " ".join(ran) + "\n"
    r = r[:-1]
    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input to the Brainetry CLI")

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--btry2bf", action="store_true", default=False,
        help="translate brainetry to brainfuck"
    )
    group.add_argument(
        "--bf2btry", action="store_true", default=False,
        help="translate brainfuck to brainetry"
    )
    group.add_argument(
        "-g", "--golf", action="store_true", default=False,
        help="golf a .btry program to single-character words"
    )

    parser.add_argument(
        "-o", "--output", metavar="output-to",
        help="path to file to write output to; use with --bf2btry or --btry2bf"
    )

    args = parser.parse_args()
    if args.input:
        if args.input.endswith(".bf") or args.input.endswith(".btry"):
            with open(args.input, "r") as f:
                inp = f.read()
        else:
            inp = args.input

        if args.btry2bf:
            r = btry2bf(inp)
            print(r)
        elif args.bf2btry:
            ops, r = bf2btry(inp)
            print(ops)
            print(r)
        elif args.golf:
            if not args.input.endswith(".btry"):
                parser.print_help()
                sys.exit(0)
            r = golf(inp)
            print(r)
            print(f"Golfed from {len(inp)} to {len(r)} bytes.")
        else:
            E(inp)
            r = ""

        if (outfile := args.output) and r:
            with open(outfile, "w") as f:
                f.write(r)
