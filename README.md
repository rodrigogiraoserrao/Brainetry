# **Brainetry**

**Brainetry** is an [esoteric programming language][eso-pl] inspired in [brainf*ck][brainfuck] and [Poetic][poetic]. Its name is a (bad) play on "brainf*ck" and "poetry".

# Coding in **Brainetry**

**Brainetry** builds on top of the eight operators brainf\*ck programs have. Below you can find a correspondence between the number of words in a line and the corresponding brainf\*ck operators. The `»` and `«` operators are new in **Brainetry** and are _not_ inherited from brainf\*ck.

| Words in a line | (brainf*ck) operator |
|-----------------|--------------------|
| 0 | `«` |
| 1 | `»` |
| 2 | `>` |
| 3 | `<` |
| 4 | `+` |
| 5 | `-` |
| 6 | `,` |
| 7 | `.` |
| 8 | `[` |
| 9 | `]` |

**Brainetry** program execution happens on top of a tape that can be extended indefinitely in both directions and whose values wrap at `256`. The tape starts out as a single cell with a value of `0` and whenever the tape pointer moves out of the tape, a new cell with the value `0` is created, extending the tape. The operator `«` sends the pointer to the left edge of the tape and the `»` operator sends the pointer to the right edge of the tape.

For **Brainetry**, a "word" is any sequence of non-space characters, so the line `"   thisis 1 really       weirdly formatted    line "` counts as having `6` words.

If you don't know how to code in brainf*ck you will have a hard time coding in **Brainetry**.

# Usage

The easiest way to run a **Brainetry** program is by saving it in a `.btry` file and passing it to the CLI explained below.

## Command Line Interface

The command line interface (`cli.py`) can

 - interpret **Brainetry** code;
 - translate "extended" brainf\*ck code into **Brainetry** by making use of the [infamous Lorem Ipsum placeholder text](https://www.lipsum.com/);
 - translate **Brainetry** code into "extended" brainf\*ck code (using the `«` and `»` operators that aren't really from brainf\*ck).

Running `cli.py -h` you get this help message:

```
usage: cli.py [-h] [--btry2bf | --bf2btry | -g] [-o output-to] input

positional arguments:
  input                 input to the Brainetry CLI

optional arguments:
  -h, --help            show this help message and exit
  --btry2bf             translate brainetry to brainfuck
  --bf2btry             translate brainfuck to brainetry
  -g, --golf            golf a .btry program to single-character words
  -o output-to, --output output-to
                        path to file to write output to; use with --bf2btry or --btry2bf
```

The `input` argument is assumed to be a file path if it ends with `.btry` (for **Brainetry** source files) or `.bf` (for brainf\*ck source files). Otherwise the `input` argument is used as the code for the CLI.

 > For example, running `cli.py btry/yacat.btry` runs one of the sample examples in this repository.

## `--bf2btry`

The `--bf2btry` flag is a utility flag. It allows you to first write your program in "extended" brainf\*ck and then get it converted to a sequence of integers corresponding to your line lengths. Additionally, a sample implementation is given as output, using the Lorem Ipsum text as a placeholder.

 > For example, the first line of output you get after running `cli.py ",[<,]»[.<]" --bf2btry` is `[6, 8, 3, 6, 9, 1, 8, 7, 3, 9]`, which corresponds to the number of words of each line in the `btry/yacat.btry` file.

## `--btry2bf`

The `--btry2bf` flag is another utility flag. It converts a **Brainetry** program to "extended" brainf\*ck and can be used to help debug your **Brainetry** programs.

 > For example, running `cli.py btry/yacat.btry --btry2bf` gives as output `,[<,]»[.<]`.

## `-g`, `--golf`

This `--golf` flag is another utility flag used to convert a **Brainetry** program into its single-character words version.

## `-o`, `--output`

The `-o` flag can be used to also write the CLI output to the given file.

# Example programs

The examples that follow have the corresponding source code in the `btry` directory.

## CAT program

This program in `btry\cat.btry` takes input and outputs it to the user.

```
This program you are currently reading
has the particularity of explaining itself. In fact,
this program has one simple mission :
Take some input provided by you
and throw it right back at your face !!!
```

## Infinite loop

This program in `btry\infinite.btry` loops forever doing nothing.

```
This program is useless.
This program is useless because it runs forever.
This program is useless because it does absolutely nothing.
```

## Another CAT program

This program in `btry\acat.btry` also takes user input and outputs it back to the user, but makes (superfluous) use of the **Brainetry** `«` operator.

```
This Brainetry program takes some input
and then proceeds to outputting much like cat.
Except for
one small teeny weeny little detail:
It uses an operator that is unique to Brainetry.

The empty line operator, whose purpose is to
reset the tape pointer to the beginning.
Lovely, right?
Some day I'll use it for the greater good.
```

## Yet another CAT program

This program in `btry\yacat.btry` does the same, but uses the **Brainetry** `»` operator.

```
This is yet another cat program.
This one, unlike the first one, is NOT
native brainf*ck code.
This one, like the previous one,
uses an operator that was freshly introduced in Brainetry:
«
This is the operator that I will use
to code YET another cat program ...
Tired yet ???
I am definitely done with these repeated cat programs.
```

## Hello, World!

This program in `btry\hello_world.btry` outputs the string `"Hello, World"` to the user.

```
This is a "short"
brainetry program that outputs, to stdout, the message
"Hello, World!" as per the
programming world standard. This standard
dictates that
a user that is trying
a language for the first time should write
as its
first program
this "Hello, World!" program.
Of course,
this becomes a repetitive task,
this becomes a repetitive task,
this becomes a repetitive task,
this becomes a repetitive task,
this becomes a repetitive task,
but that shouldn't
hinder you from
tackling this awesome challenge in the Brainetry programming language.
Me, myself and
I have found this language
to be quite amusing if
used to write
self-referential programs like this one.
Self-referential objects are objects that
I, personally, really enjoy. This
might be because I am just a weird person.
Or not!
Who knows? Certainly not me.
Dear reader, please rest assured that we
are ALMOST
at the
MIDDLE of
this self referential program.
Also, please refraing from adding the hyphen
between self
and referential
in the line above, as it is
NOT a typo, it is missing purposefully.
A very important skill
needed to write Brainetry
programs is one's imagination.
This is because each instruction needs one line
of Brainetry source code on its own.
Sounds easy?
I can assure you, it definitely is not easy.
I'm growing tired,
I'm growing unimaginative,
I'm growing old,
I'm writing code.
Oh boy, I wish that would've rhymed!
Even though I can't
really rhyme in English
because I am unskilled,
I can tell you that this is
exhibiting signs of schizophrenia, right?
At this point I am
pretty much talking to myself,
and no one is listening,
right? No one is listening,
right? I definitely hope not.
Now on to some decent source code,
this program works
by harnessing the
well known power of modular
arithmetic, a really nice thing mathematics has
bestowed upon
us, mortals.
This is,
for real,
a really awesome gift
from the mathematicians of yor to us.
```

# Implementation

The implementation - in Python - can be found in the `brainetry.py` file; notice that the Python style used in that file was a proof of concept for something unrelated to this project and thus may strike as weird Python code.

The implementation can be restyled into:

```py
def I(l, i, p=0, m=[0]):
    while l:
        n, *l = l
        if n in [0, 1]:
            p = n*(len(m) - 1)
        elif n in [2, 3]:
            p += 1 - [2, 0, 3].index(n)
            m = [0]*(p<0) + m + [0]*(p==len(m))
            p = max(0, p)
        elif n in [4, 5]:
            m[p] += 1 - [4, 0, 5].index(n)
            m[p] %= 256
        elif 6 == n:
            if not i:
                i = "\u0000"
            c, *i = i
            m[p] = ord(c)
        elif 7 == n:
            print(chr(m[p]), end="")
        elif 8 == n:
            t = 1
            g = [t := t + (k==8) - (k==9) for k in l].index(0)
            while m[p]:
                i, p, m = I(l[:g], i, p, m)
            l = l[g:]
    return i, p, m

def E(c):
    l = [*map(len, filter(
        bool,
        [l.split(" ")for l in c.split("\n")]
    ))]
    I(l, input(" inp >> "))
    print()
```

[eso-pl]: https://en.wikipedia.org/wiki/Esoteric_programming_language
[brainfuck]: https://esolangs.org/wiki/Brainfuck
[poetic]: https://mcaweb.matc.edu/winslojr/vicom128/final/
