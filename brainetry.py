#!/usr/bin/python3
"""
Command Line Interface (CLI) for the Brainetry programming language.
"""

import argparse
import sys

import interpreter

def btry2symb(code):
    """Translate a brainetry program to symbolic operators."""

    result = ""
    for line in code.split("\n"):
        n = len([*filter(bool, line.split(" "))])
        n += 16*(len(line) > 1 and line[-1] == line[-2])
        if n >= len(interpreter.O):
            continue
        result += interpreter.O[n]
    return result

def symb2btry(code):
    """Translate symbolic operators to brainetry."""

    from lorem import lorem

    while "\n" in lorem:
        lorem = lorem.replace("\n", " ")
    while "  " in lorem:
        lorem = lorem.replace("  ", " ")
    lorem = lorem.split(" ")

    result = ""
    source = lorem[::]
    hexs = []
    for c in code:
        if c == "\n":
            result += c
        if c in interpreter.O:
            i = interpreter.O.index(c)
            mi, bi = divmod(i, 16)
            hexs.append(f"{i:02x}")
            if bi > len(source):
                source += lorem[::]
            new = " ".join(source[:bi])
            if mi&1:
                new += new[-1]
            source = source[bi:]
            result += new + "\n"
    result = result[:-1]

    return hexs, result

def golf(inp):
    """Golf a brainetry program."""

    r = ""
    for line in inp.split("\n"):
        ran = range(len([*filter(bool, line.split(" "))]))
        ran = ["abcdefghijklmno"[i] for i in ran]
        r += " ".join(ran)
        if len(line) > 1 and line[-1] == line[-2]:
            r += r[-1]
        r += "\n"
    r = r[:-1]
    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="source code/file to the brainetry CLI")
    parser.add_argument("-d", "--debug", metavar="level", type=int, nargs="?", const=0,
        help="debug [define nest level]"
    )
    parser.add_argument("-w", "--wrap-at", metavar="cell_size", type=int, default=256,
        help="cells wrap at this value (defaults to 256); use 0 for no wrapping"
    )
    parser.add_argument("--numeric-io", action="store_true", default=False,
        help="whether I/O should act on numbers (defaults to false)"
    )
    parser.add_argument(
        "-o", "--output", metavar="file", help="also save output to file"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--btry2symb", action="store_true", default=False,
        help="translate brainetry to symbolic operators"
    )
    group.add_argument("--symb2btry", action="store_true", default=False,
        help="translate symbolic operators to brainetry"
    )
    group.add_argument("-g", "--golf", action="store_true", default=False,
        help="auto-golf a .btry program"
    )

    args = parser.parse_args()
    if args.source:
        # Get input from the correct source
        if args.source.endswith(".sbtry") or args.source.endswith(".btry"):
            print("(Brainetry CLI: reading source code from file.)")
            with open(args.source, "r", encoding="utf8") as f:
                inp = f.read()
        else:
            print("(Brainetry CLI: assuming literal input.)")
            inp = args.source

        if args.btry2symb:
            r = btry2symb(inp)
            print(r)
        elif args.symb2btry:
            hexs, r = symb2btry(inp)
            print(f"Hex values: {', '.join(hexs)}")
            print(r)
        elif args.golf:
            if not args.source.endswith(".btry"):
                parser.print_help()
                sys.exit(0)
            r = golf(inp)
            print(r)
            print(f"Golfed from {len(inp)} to {len(r)} bytes.")
        else:
            env = {
                "W": args.wrap_at,
                "NIO": args.numeric_io,
            }
            debug = args.debug or 0
            i, p, m, r = interpreter.E(inp, de=debug, env=env)
            if args.debug is not None:
                print(f"Final state:")
                print(f"\tm[{p}]={m[p]} @ {interpreter.mpp(m, p)}")
                if i is None:
                    print("No input was consumed by the program.")
                else:
                    print(f"Input left to consume: '{interpreter.lpp(i)}'")
                print(f"Output produced: '{r}'")

        if (outfile := args.output) and r:
            with open(outfile, "w", encoding="utf8") as f:
                f.write(r)
