#!/usr/bin/env python3
#-*- coding: utf_8 -*-
# dbfview.py - A simple DBF file viewer using curses

import subprocess
import os, sys
if os.name == 'posix':
    import curses
elif os.name == 'nt':
    import unicurses as curses
else:
    print("Unsupported OS")
    sys.exit(1)

def hexread(bts):
    """
    Return a hexadecimal representation of a byte string.
    """
    nums = [str(num).zfill(2) for num in range(len(bts))]
    hexs = [hex(n).strip('0x').upper().zfill(2) for n in bts]
    chars = [chr(n).rjust(2) if 32 <= n <= 126 else ' .' for n in bts]


    return nums, hexs, chars

def openfile(filename):
    fd = None
    try:
        fd = open(filename, 'rb')
    except:
        pass
    return fd

def show(stdscr, *args):
    """
    Hexadecimal dump of a binary file using curses.
    """
    lfiles = [openfile(f) for f in args]
    lbytes = [f.read(32) for f in lfiles]
    fbytes = [f.read()[-1] for f in lfiles]
    results = [hexread(bts) for bts in lbytes]

    try:
        curses.cbreak()
    except:
        pass
    
    stdscr.keypad(True)

    curses.set_escdelay(25)

    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Unselected text
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)  # Unselected text
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)  # Unselected text
    if curses.can_change_color():
        # Define a custom dark green color (RGB values are in the range 0-1000)
        curses.init_color(10, 0, 350, 0)  # Custom dark green color
        curses.init_pair(4, curses.COLOR_WHITE, 10)  # Unselected text with custom dark green background
    else:
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN | curses.COLOR_YELLOW)  # Unselected text

    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Selected text

    curses.curs_set(0)

    # Set default background color to blue
    stdscr.bkgd(' ', curses.color_pair(1))

    # Print the hexadecimal dump
    start = 1
    for index, t in enumerate(results):
        fbyte = [fbytes[index]]
        lbyte = hexread(fbyte)[1][0]
        stdscr.addstr(start, 0, f"File: {args[index]} - Endswith: {lbyte}".ljust(95), curses.color_pair(4))
        stdscr.addstr(start + 1, 0, " ".join(t[0]), curses.color_pair(5))
        stdscr.addstr(start + 2, 0, " ".join(t[1]), curses.color_pair(2))
        stdscr.addstr(start + 3, 0, " ".join(t[2]), curses.color_pair(3))
        start += 5

    while True:
        key = stdscr.getch()

        # Handle key inputs
        if key == ord('q') or key == ord('Q') or key == 27:  # Quit on 'q', 'Q' or ESC
            break

def main():
    if len(sys.argv) < 2:
        print("Usage: python hexreader <filename>")
        sys.exit(1)
    try:
        curses.wrapper(lambda stdscr: show(stdscr, *sys.argv[1:6]))
    except curses.error as e:
        subprocess.run(["clear"])
        sys.stderr.write(f"Error initializing curses: {e}\n")
        sys.stderr.flush()
        sys.exit(1)
    except KeyboardInterrupt as e:
        subprocess.run(["clear"])
        sys.exit(0)

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
