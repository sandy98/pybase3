#-*- coding: utf_8 -*-
# This file is the main entry point for the pybase3 package.

#print("Coming soon...")

from re import sub
import os, sys, subprocess

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
