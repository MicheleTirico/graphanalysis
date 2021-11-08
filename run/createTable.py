"""
create table of analysis
input:  files csv
output: table csv

"""
import csv
import sys
import os
import pandas as pd
#     pathIN = "/data/results/gpd_indicators.csv"

def main(args):
    pathIN, pathOUT  = args[0],args[1]
    table = pd.read_csv(pathIN,sep=",")
    df = pd.DataFrame(data=table)

    del df["tota"]
    del df["aver.1"]
    del df["Unnamed: 10"]

    df.round(3)
    print(df.keys())
    print(df)
    df.to_csv(pathOUT, sep=",")

"""
    dfStat=df.describe()

    for i in range(len(l_min)) : l_min[i]= "{:.3f}".format(float(l_min[i]))
    for i in range(len(l_min)) : l_max[i]= "{:.3f}".format(float(l_max[i]))
    for i in range(len(l_min)) : l_mea[i]= "{:.3f}".format(float(l_mea[i]))

    f = open(pathOUT, "w",newline="")
    w = csv.writer(f)
    l_min.insert(0,name)
    l_max.insert(0,name)
    l_mea.insert(0,name)


    l_min.insert(1,"min")
    l_max.insert(1,"max")
    l_mea.insert(1,"mea")

    w.writerow(l_max)
    w.writerow(l_min)
    w.writerow(l_mea)

    print (l_min,l_max,l_mea,sep="\n")

"""

if __name__ == "__main__":
    main(sys.argv[1:])
