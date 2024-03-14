#!/usr/bin/env python

import csv
import sys

def main (argv):

    dataFilename1 = argv[1]
    dataFilename2 = argv[2]

    try:
        fileData1 = open(dataFilename1, encoding="utf-8")
        fileData2 = open(dataFilename2, encoding="utf=8")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
            dataFilename1, err), file=sys.stderr)
        print("Unable to open names file '{}' : {}".format(
            dataFilename2, err), file=sys.stderr)
        sys.exit(1)

    dataSet1 = csv.reader(fileData1)
    dataSet2 = csv.reader(fileData2)

    


main (sys.argv)