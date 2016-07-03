# !/usr/bin/python3
"""Rename files.

Rename files containing `-` with `_`
"""
import os

# Directory to traverse
walk = os.walk('./Test/')

# A file containing filenames that you want to change.
# Already generated
with open("filenames.txt") as filenames_to_change:
    names = filenames_to_change.read().splitlines()

for dirpath, dirs, files in walk:
    for filename in files:
        fpath = os.path.join(dirpath, filename)

        for name in names:
            old_name = name
            new_name = name.replace('-', '_')
            print("{} >>> {}".format(old_name, new_name))

            with open(fpath) as f:
                s = f.read()
            s = s.replace(old_name, new_name)
            with open(fpath, "w") as f:
                f.write(s)

