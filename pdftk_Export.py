
#import pathlib #path
import subprocess
import sys
import os

import re

'''
Version2.1.Uses pdftk to extract pages from one pdf to creater another

'''

# uses pdftk to get dump information
def getPageNumb(filename):

    pgnum = ""
    l = []

    #cmd = f"pdftk {filename} dump_data | findstr NumberOfPages"
    cmd = "pdftk {} dump_data".format(filename)
    # print(cmd)
    command = cmd.split()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
    except Exception as e:
        print("exception", e)
    else:
        for line in output.splitlines():
            #print(f"Got line: {line}")
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
    info = ["A" + i for i in info] #https://stackoverflow.com/a/15738282/14451841
    print("info :" , info)
    # List -> str
    info = " ".join(info)
    print("info :" , info)

    #pdftk A=in.pdf cat A1-10 A15 A17 output out.pdf   #https://askubuntu.com/a/282455 See comment

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
    pages = raw_input("Pages for extraction? ") #input for some reason evaluates it. eval(input()). I think i might be using python 2 or something but the system shows 3.7.2 #https://stackoverflow.com/a/4915366/14451841
    print("pages :", pages)
    if pages == "": #https://stackoverflow.com/a/23979260/14451841
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


#for testing in wing ide only
#n = getPageNumb("in.pdf")
#outName = askForFNameOut()
#extractpages("in.pdf", "1 , 2-4 ,  5 ", outName)


for filename in sys.argv[1:]:
    #print(filename)
    n = getPageNumb(filename) # get total page number
    pp = askForPages()
    outName = askForFNameOut()
    extractpages(filename, pp, outName)
    input('Press ENTER to exit') #https://stackoverflow.com/a/15821059/14451841
