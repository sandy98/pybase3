#-*- coding: utf_8 -*-
# This file is the main entry point for the pybase3 package.

#print("Coming soon...")

import os, sys, subprocess
from argparse import ArgumentParser
try:
    from pybase3 import __version__, __author__, __email__, __license__, __url__, __description__   
except ImportError:
    from . import __version__, __author__, __email__, __license__, __url__, __description__

def info():
    print(f"pybase3 {__version__} by {__author__}")
    print(f"Email: {__email__}")
    print(f"License: {__license__}")
    print(f"URL: {__url__}")
    print(f"Description: {__description__}")
    sys.exit(0)

def showdbfs():
    dbfs = []

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower().endswith(".dbf"):
                dbfs.append((file, os.path.join(root, file))) 

    dbfs.sort(key=lambda x: x[0])

    title = f"{len(dbfs)} DBF files found:"
    subtitle = "-" * len(title)
    subprocess.run(["clear"])
    print(title, "\n", subtitle, sep="")
    print()
    entries=""
    for index, entry in enumerate(dbfs):
        entries += f"{index+1}. {entry[0]}\t"
    print(entries)

    resp = input(f"\nSelect a DBF file to view (1-{len(dbfs)}) or <Enter> to quit: ")
    if resp.isdigit():
        index = int(resp) - 1
        if 0 <= index < len(dbfs):
            filename = dbfs[index][1]
            print(f"\nOpening {filename}...")
            try:
                subprocess.run(["dbfview", filename])
            except KeyboardInterrupt as e:
                subprocess.run(["clear"])
                print("\nUser interrupted.")
                sys.exit(0)
        else:
            print("\nInvalid selection.")

    print("Good bye!")
    sys.exit(0)    

def main():
    parser = ArgumentParser(description="A simple library to read and write dbase III files.")
    parser.add_argument("-v", "--version", action="version", version=f"pybase3 {__version__}")
    parser.add_argument("-i", "--info", action="store_true", help="Shows information about the package.")
    args = parser.parse_args()

    if args.info:
        info()
    else:
        showdbfs()

if __name__ == "__main__":
    main()  

