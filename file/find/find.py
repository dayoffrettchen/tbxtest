from __future__ import print_function
import os
import shutil


def directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


herbst_ = u"/home/dume/herbst/Sicherung_Leipzig/NB-Herbst/"
print("Look for", herbst_)
walk = os.walk(herbst_)
for root, dirs, files in walk:
    for file in files:
        if root.find("Projekt") >= 0:
            if file.endswith(".png") or file.endswith(".jpg"):
                relPath = root.strip(herbst_)
                print(relPath)
                path = "/home/dume/test/" + relPath
                directory(path)
                shutil.copyfile(os.path.join(root, file), os.path.join(path, file))
                print(os.path.join(root, file))

