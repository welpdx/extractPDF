


import subprocess
import sys
import os
import shutil
import re

'''
Version1. Get total NumberOfPages of input file
1. uses pdftk to get dump information
2. Scan each line for "NumberOfPages"
3. extract the numbers from the line

'''


data = ""

def getPageNumb(filename):
    #fn = pathlib.Path(filename)
    global data
    l = []
    #cmd = f"pdftk {filename} dump_data | findstr NumberOfPages"
    cmd = "pdftk {} dump_data".format(filename)
    print(cmd)
    command = cmd.split()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
    except Exception as e:
        print("exception", e)
    else:
        for line in output.splitlines(): # https://stackoverflow.com/a/3437070/14451841
            #print(f"Got line: {line}")
            if "NumberOfPages" in line:
                l = [int(s) for s in line.split() if s.isdigit()] # https://stackoverflow.com/a/4289557/14451841
                data = l[0]


    print("data :", data)

def extractpages():
    # ask for info
    # make a
    return True




#n = getPageNumb("in.pdf") # for testing using ide only


for filename in sys.argv[1:]:
    print(filename)
    n = getPageNumb(filename)
