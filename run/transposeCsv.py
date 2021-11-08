"""
Transpose csv
From a csv file we transpose the data (rows become columns)
in:     the path of the data (csv)
out:    the path of the result (csv)
"""

# import csv
from csv import reader, writer
import sys

def main(args):
    pathIN, pathOUT = args[0],args[1]
    with open(pathIN) as f, open(pathOUT, 'w') as fw:
        writer(fw, delimiter=',').writerows(zip(*reader(f, delimiter=',')))

if __name__ == "__main__":
    main(sys.argv[1:])
