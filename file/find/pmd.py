#!/usr/bin/env python
from subprocess import call
import xml.etree.ElementTree as ET
import argparse

old = "./qa/pmd_report_old.html"
new = "./qa/pmd_report.html"
xml = "./qa/pmd.xml"
__author__ = 'christoph'

start = "/home/dume/tapina/"

parser = argparse.ArgumentParser(description="optional to write")
parser.add_argument("--print", dest="prnt",  type=bool, help="if u want to print everything the file", default=False)
parser.add_argument("--write", dest="write",  type=bool, help="if u want to write the file", default=False)
prnt = parser.parse_args().prnt
write = parser.parse_args().write

call(["ant", "pmd"])
tree = ET.parse(start + xml)
verbose = False
nr = 0
toWrite = ""
for file in tree.getroot():
    toWrite += "\n"
    for violation in file:
        nr += 1
        if verbose:
            toWrite += ( ": " + file.get("name") + "(" + violation.get("beginline") + "," + violation.get(
                'endline') + ")[" + violation.get('rule') + "] " + violation.text)
        else:
            toWrite += ( ": " + file.get("name") + "(" + violation.get("beginline") + "," + violation.get(
                'endline') + ")[" + violation.get('rule') + "] " )
        toWrite += "\n"

if prnt:
    print(toWrite)

old_ = start + "pmd_old"
new_ = start + "pmd_new"
toWriteFile = open(new_, "w+")
oldPmds = open(old_, "r+")
oldLines = oldPmds.readlines()
toWriteFile.write(toWrite)
call(["diff", old_, new_])
if write:
    oldPmds = open(old_, "w+")
    oldPmds.write(toWrite)

