import shutil
import sys
import time
from random import choice, randrange, paretovariate, random


def getchars(_start, _end):
    return [chr(i) for i in range(_start, _end + 1)]


black, green, white = "30", "32", "37"
FRAME_DELAY = 0.075
chars = (
        getchars(2308, 2361) + getchars(2392, 2401) + getchars(2418, 2431) + getchars(2437, 2443) + getchars(2451, 2472)
)


def pr(command):
    print("\x1b[", command, sep="", end="")


def pareto(lines):
    number = (paretovariate(1) - 1) * lines
    return max(0, lines - number)


def print_at(char, x, y, color):
    pr(f"\x1b[{y};{x}f\x1b[1;{color}m")
    print(char, end="", flush=True)


def cascade(col, lines):
    line = 0
    eline = -1
    erasing = False
    limit = pareto(lines)
    while True:
        line = line + 1
        if line < limit:
            print_at(choice(chars), col, line - 1, green)
            print_at(choice(chars), col, line, white)
        elif erasing:
            eline = eline + 1
            print_at(" ", col, eline, black)
        else:
            erasing = randrange(line + 1) > (lines / 2)
            eline = 0
        yield None
        if eline >= limit:
            print_at(" ", col, line, black)
            break


def add_new(cascading, cols, lines):
    if random() > 0.1:
        col = randrange(cols)
        cascading.add(cascade(col, lines))
        return True
    return False


def iterate(cascading):
    stopped = set()
    for c in cascading:
        try:
            next(c)
        except StopIteration:
            stopped.add(c)
    return stopped


def main():
    try:
        cols, lines = shutil.get_terminal_size()
        pr("2J")  # clear screen
        pr("?25l")  # Hides cursor
        pr("s")  # Saves cursor position
        cascading = set()
        while True:
            while add_new(cascading, cols, lines):
                pass
            stopped = iterate(cascading)
            sys.stdout.flush()
            cascading.difference_update(stopped)
            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        pass
    finally:
        pr("m")  # reset attributes
        pr("2J")  # clear screen
        pr("u")  # Restores cursor position
        pr("?25h")  # Show cursor


if __name__ == "__main__":
    main()
