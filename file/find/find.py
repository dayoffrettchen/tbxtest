from __future__ import print_function
import os
import shutil
import sys, getopt

def directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def main(argv):
    options, args = getopt.getopt(("position","i"))

    for opt, arg in options:
        if opt == "-f":
            fromDirectory = opt
        if opt == "-t":
            toDirectory = opt
    print("Look for", fromDirectory)
    walk = os.walk(fromDirectory)
    for root, dirs, files in walk:
        for file in files:
            if root.find("Projekt") >= 0:
                if file.endswith(".png") or file.endswith(".jpg"):
                    relPath = root.strip(fromDirectory)
                    print(relPath)
                    path = toDirectory + relPath
                    directory(path)
                    shutil.copyfile(os.path.join(root, file), os.path.join(path, file))
                    print(os.path.join(root, file))

