
#import pathlib #path
import subprocess
import sys
import os
#import shutil #for removing files
import re

'''
Version3. Uses pdftk to extract pages from one pdf to creater another
Cleaned up.
Todo:
    1. Delete out.pdf if detected.
    2. Create Sub folder?

'''

# uses pdftk to get dump information
def getPageNumb(filename):
    pgnum = ""
    l = []
    cmd = "pdftk {} dump_data".format(filename)
    command = cmd.split()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
    except Exception as e:
        print("exception", e)
    else:
        for line in output.splitlines():
            if "NumberOfPages" in line:
                l = [int(s) for s in line.split() if s.isdigit()]
                pgnum = l[0]
    print("Pages in Document :", pgnum)
    return pgnum



# Uses gathered input to extract pdf pages
def extractpages(filename, info, filenameOut):

    # str -> list
    info = info.split(",")
    # strip white spaces in each item of the list
    info = [ l.strip() for l in info]
    # Add A in front of every item of the list
    info = ["A" + i for i in info]
    print("info :" , info)
    # List -> str
    info = " ".join(info)
    print("info :" , info)
    cmd = "pdftk A={} cat {} output {}".format(filename, info, filenameOut)
    print(cmd)
    command = cmd.split()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
    except Exception as e:
        print("exception", e)
    else:
        for line in output.splitlines():
            print("Got line: {}".format(line))

    return

# prompt for pages to extract
def askForPages():
    pages = raw_input("Pages for extraction? ")
    print("pages :", pages)
    if pages == "":
        print("Error Selection. Please Try again.")
        askForPages()
    else:
        return str(pages)

# prompt for output filename
def askForFNameOut():
    fName = ""
    fName = raw_input("Output file name? (xxx.pdf) (Defalt = out.pdf):")
    if fName == "":
        print("You pressed Enter. Output file name = out.pdf")
        return "out.pdf"
    else:
        return fName + ".pdf"




for filename in sys.argv[1:]:
    n = getPageNumb(filename)
    pp = askForPages()
    outName = askForFNameOut()
    extractpages(filename, pp, outName)
    input('Press ENTER to exit')
