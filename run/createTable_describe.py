"""
create table of analysis
input:  files csv
output: table csv

"""
import csv
import sys
import os
import pandas as pd
import numpy as np

#     pathIN = "/data/results/gpd_indicators.csv"

def main(args):
    print("parameters: \n0 -> pathIn \n1 -> pathOut \n2 -> name file")
    pathIN, pathOUT,name  = args[0],args[1],args[2]
    print (pathIN, pathOUT,name)
    table = pd.read_csv(pathIN,sep=",")
    df = pd.DataFrame(data=table)
    del df["tota"]
    del df["aver.1"]
    del df["Unnamed: 10"]

    dfStat=df.describe()
    print(dfStat)
    l_keys = list(df.keys())
    l_min = list(df.min())[1:]
    l_max = list(df.max())[1:]
    l_mea = list(df.mean())[1:]
    l_cvar= list(df.std()[1:] / df.mean()[1:])

    # [(np.sd(df[i])/np.mean(df[i])) for i in range(1,len(l_keys))]
    print (l_cvar)

    for i in range(len(l_min)) : l_min[i]= "{:.3f}".format(float(l_min[i]))
    for i in range(len(l_min)) : l_max[i]= "{:.3f}".format(float(l_max[i]))
    for i in range(len(l_min)) : l_mea[i]= "{:.3f}".format(float(l_mea[i]))
    for i in range(len(l_min)) : l_cvar[i]= "{:.3f}".format(float(l_cvar[i]))

    f = open(pathOUT+name+".csv", "w",newline="")
    w = csv.writer(f)
    l_min.insert(0,name)
    l_max.insert(0,name)
    l_mea.insert(0,name)

    l_cvar.insert(0,name)
    l_keys.insert(1,"stat")
    l_min.insert(1,"min")
    l_max.insert(1,"max")
    l_mea.insert(1,"mean")
    l_cvar.insert(1,"coef.var")

    w.writerow(l_keys)
    w.writerow(l_max)
    w.writerow(l_min)
    w.writerow(l_mea)
    w.writerow(l_cvar)

    print (l_keys,l_min,l_max,l_mea,l_cvar,sep="\n")

if __name__ == "__main__":
    main(sys.argv[1:])
