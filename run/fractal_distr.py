"""
create a histogram of fractal dimensions
in: list of csv fractal
out:png
"""
import math as mt
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter
sys.path.append("../tools")

from tools import *


def main(args):
    print("parameters: \n0 -> pathIn \n1 -> pathOut ")
    pathIN, pathOut = args[0],args[1]
    fractalDim = []
    patterns = ["holes", "mazes", "solitons", "movingSpots"]
    dic = {}
    for p in patterns: dic[p] = []
    print (patterns)
    for file in os.listdir(pathIN):
        if "csv" and "fractal" in str(file) and "png" not in str(file):
    #        print(file)
            pattern = getPattern(str(file))
            data = pd.read_csv(pathIN +file,sep=";")
            v = list(data["val"])
            minBox = 1
            val = v[minBox:]
            val = [float(i) for i in val]
            size = [i for i in range(1,len(val)+1) ]
            val = [mt.log(i) for i in val]
            size = [mt.log(i) for i in size]
            m,b = np.polyfit(size,val,1)
            fractalDim.append(abs(m))
            size, val= listRem(size,val)
            l = dic[pattern]
            l.append(abs(m))
            dic[pattern] = l

    fig, ax = plt.subplots()
    ax.set_title("fractal dimension")
    ax.set_ylabel("probability")
    ax.set_xlabel("fractal dimension")
    plt.yticks([i*0.5 for i in range (0,10)])
    vals=[]
    for p in patterns: vals.append(dic[p])
#    vals.append(dic["holes"])
    plt.hist(vals,  bins=10,density=True, cumulative=False, stacked=False, label=patterns )

    ax.yaxis.set_major_formatter(PercentFormatter(xmax=len(vals)/0.5))
    plt.legend()
    plt.savefig(pathOut)

    plt.show()




if __name__ == "__main__":
    main(sys.argv[1:])
