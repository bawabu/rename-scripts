import os

walk = os.walk("./app/")

for dirpath, dirs, files in walk:
    for filename in files:
        fpath = os.path.join(dirpath, filename)
        with open("filenames.txt", "a") as f:
            f.write(filename + "\n")
