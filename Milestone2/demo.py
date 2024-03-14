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

    dataSet1 = csv.reader(fileData) 
    
    for rowDataFields in dataSet1:
        date = rowDataFields[0]
        place = rowDataFields[1]
        occupation = rowDataFields[3]
        expereince = rowDataFields[4]
        stats = rowDataFields[5]

        if "Less than 1 year" in expereince:
            print("{},{},{},{},{}".format(date, place, occupation, expereince, stats))    


    fileData.close()

main (sys.argv)
