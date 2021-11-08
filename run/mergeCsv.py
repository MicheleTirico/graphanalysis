"""
the script have as input a set of csv files. Each of them, have 2 colums, the first column is in common to all others files.
The output is a csv, where each row is the second column.
in:     a set of csv files
out:    a csv file
"""

import csv
import sys
import os
import pandas as pd

def main(args):
    pathIN, pathOUT = args[0],args[1]
    files = os.listdir(pathIN)
    os.system("rm " +pathOUT )
    os.system("touch " +pathOUT)
    p= 0

    with open(pathOUT, "w",newline="") as file :
        for f in os.listdir(pathIN):
            name = str(os.path.splitext(f)[0])
            writer = csv. writer(file)
            table = pd.read_csv(pathIN+"/"+f, sep=";")
            c = [name] + list (table.val)
            writer.writerow (c)
            print(p, name)
            p+=1

if __name__ == "__main__":
    main(sys.argv[1:])
