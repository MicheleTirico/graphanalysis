"""
create the fractal dimension of a list of networks and the borders from an other list
in: list of CSV for borders
    list of CSV for list
out:png
"""

import math as mt
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sys.path.append("../tools")

from tools import *

def main (args):
    pathIN, nameFile = args[0],args[1]
    print (pathIN, nameFile)
    fig, ax = plt.subplots()
    ax.set_title("fractal dimension")
    ax.set_ylabel("log of number of not empty boxes (N(r))")
    ax.set_xlabel("log of number of boxes (r)")
    valMin , valMax = [100 for i in range (1000)] , [0 for i in range (1000)]
    fractalDim = []
    patterns = ["holes", "mazes", "solitons", "movingSpots"]
    colors = ["red", "green","blue","purple"]
    for file in os.listdir(pathIN):
        if "csv" and "fractal" in str(file) and "png" not in str(file):
#            print(file)
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

            ax.plot(size,val, marker = ".", markersize= 0.0, linewidth=0.5, label = pattern, color = colors [patterns.index(pattern)])
            print (pattern)


#    text = "fractal dimension N(r)=r^d \nd = [{:.3f} - {:.3f}]".format( min(fractalDim),   max(fractalDim))
    plt.ylim([-.5,12])
#    plt.savefig(pathIN+nameFile+".png")
    plt.show()
    print ("png, go to ->",pathIN+nameFile+".png")



if __name__ == "__main__":
    main(sys.argv[1:])
