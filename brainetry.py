#!/usr/bin/python3
"""
Command Line Interface (CLI) for the Brainetry programming language.
"""

import argparse
import os
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
    ops_is = []
    for c in code:
        if c == "\n":
            result += c
        if c in interpreter.O:
            i = interpreter.O.index(c)
            mi, bi = divmod(i, 16)
            ops_is.append((bi, mi))
            if bi > len(source):
                source += lorem[::]
            new = " ".join(source[:bi])
            if mi&1:
                new += new[-1]
            source = source[bi:]
            result += new + "\n"
    result = result[:-1]

    return ops_is, result

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
    parser.add_argument("-d", "--debug", metavar="level", default=0, type=int,
        help="define debug nest level"
    )
    parser.add_argument(
        "-w", "--wrap-at", metavar="cell_size", type=int, default=256,
        help="cells wrap at this value (defaults to 256); use 0 for no wrapping"
    )
    parser.add_argument("--live-output", action="store_true", default=False,
        help="force program execution to print output while running"
    )
    parser.add_argument(
        "-o", "--output", metavar="file", help="redirect output to file"
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
        if args.source.endswith(".bf") or args.source.endswith(".btry"):
            print("(Brainetry CLI: reading source code from file.)")
            with open(args.source, "r") as f:
                inp = f.read()
        else:
            print("(Brainetry CLI: assuming literal input.)")
            inp = args.source

        if args.btry2symb:
            r = btry2symb(inp)
            print(r)
        elif args.symb2btry:
            ops, r = symb2btry(inp)
            print(ops)
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
                "LO": args.live_output,
                "W": args.wrap_at,
            }
            i, p, m, o = interpreter.E(inp, de=args.debug, env=env)
            if args.live_output:
                o = "(Full program output >>>\n" + o + "\n<<<)"
            print(o)
            if args.debug:
                print(f"Final state: m[{p}]={m[p]} @ {interpreter.mpp(m, p)}")
            r = o

        if (outfile := args.output) and r:
            with open(outfile, "w") as f:
                f.write(r)
