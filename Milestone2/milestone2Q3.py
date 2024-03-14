#!/usr/bin/env python

import csv
import sys

def main (argv):

    dataFilename = argv[1]

    try:
        fileData = open(dataFilename, encoding="utf-8")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
            dataFilename, err), file=sys.stderr)
        sys.exit(1)

    dataSet2 = csv.reader(fileData)    

    


main (sys.argv)