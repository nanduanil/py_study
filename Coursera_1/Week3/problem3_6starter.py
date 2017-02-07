# -problem3_6.py *- coding: utf-8 -*-

import sys

inputFile = sys.argv[1]
lengthFile = sys.argv[2]

inputFileReader = open(inputFile)
lengthFileReader = open(lengthFile,'w')

for line in inputFileReader:
    line = line.strip("\n")
    count = len(line)
    lengthFileReader.write(str(count)+"\n")
    
inputFileReader.close()
lengthFileReader.close()

    