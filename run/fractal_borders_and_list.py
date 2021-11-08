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

def listRem (l0,l1):
#    len = len(l0)
    l0n,l1n=[],[]
    eps = 0.001
    val = 0
    for i in range(0,len(l1)):
        v = l1[i]
        if abs(v - val) > eps :
#            print (v-val)
            l1n.append(l1[i])
            l0n.append(l0[i])
        val = v
    return l0n, l1n

def main (args):
    print("parameters: \n0 -> pathInBor (borders) \n1 -> pathInList (list) \n2-> pathOut to store png (give path/nameFile.png)")
    pathInBor, pathInList, pathOut =  args[0], args[1], args[2]
#    pathOutList , pathOutBor = pathOut +"_list", pathOut+"_bor"

    fig, ax = plt.subplots()
    ax.set_title("fractal dimension")
    ax.set_ylabel("log of number of not empty boxes (N(r))")
    ax.set_xlabel("log of number of boxes (r)")

    # get borders
    valMin , valMax = [100 for i in range (1000)] , [0 for i in range (1000)]
    fractalDim = []
    all = []
    for file in os.listdir(pathInBor):
        if "csv" and "fractal" in str(file) and "png" not in str(file):
    #        print(file)
            data = pd.read_csv(pathInBor +file,sep=";")
            v = list(data["val"])
            all.append(v)

    for p, line in enumerate(all) :
        minBox = 1
        val = line[minBox:]
        val = [float(i) for i in val]
        size = [i for i in range(1,len(val)+1) ]
        val = [mt.log(i) for i in val]
        size = [mt.log(i) for i in size]
        m,b = np.polyfit(size,val,1)
        fractalDim.append(m)
        i = 0
        while i < len (val) :
            if val[i] <= valMin[i]: valMin[i] = val[i]
            if val[i] >= valMax[i]: valMax[i] = val[i]
            i+=1
        valMin, valMax = valMin[0:len(val)], valMax[0:len(val)]

    # get list
    l = []
    patterns=[]
    for file in os.listdir(pathInList):
        print(file)
        if "csv" and "fractal" in str(file) and "png" not in str(file):
            patterns.append(getPattern(str(file)))
            data = pd.read_csv(pathInList +file,sep=";")
            v = list(data["val"])
            l.append(v)

    sizeMinRem, valMinRem = listRem(size,valMin)
    sizeMaxRem, valMaxRem = listRem(size,valMax)
#   print (len(sizeMinRem), len(sizeMaxRem))
#    ax.plot(sizeMinRem,valMinRem, marker = ".", markersize= 0.8, linewidth=2, color ="red")
#    ax.plot(sizeMaxRem,valMaxRem, marker = ".", markersize= 0.8, linewidth=3, color ="red")
#   "cities [{:.3f} - {:.3f}] of cities".format( min(fractalDim),   max(fractalDim))
    ax.fill_between(sizeMaxRem, valMaxRem,   color ="#DCDCDC",label="explore (d=[{:.3f} - {:.3f}])".format( abs(min(fractalDim)),   abs(max(fractalDim)))) # "#5f5f5f")
    ax.fill_between(sizeMinRem, valMinRem,   color ="white",) # "#5f5f5f")

    fractalDimList = []
    a = 0
    for p, line in enumerate(l) :
        minBox = 1
        val = line[minBox:]
        val = [float(i) for i in val]
        size = [i for i in range(1,len(val)+1) ]
        val = [mt.log(i) for i in val]
        size = [mt.log(i) for i in size]
        m,b = np.polyfit(size,val,1)
        fractalDimList.append(m)
        l0,l1 = listRem(size,val)
        ax.plot(l0,l1, marker = ".", markersize= 5, linewidth=.0,label=str(patterns[p])+" (d="+"{:.3f}".format(abs(m)) +")")
        a+=1
#        ax.plot(size,val, marker = ".", markersize= 2, linewidth=.0)

    fractalDim = [abs(i) for i in fractalDim]
#    ax.plot(size,valMin, marker = ".", markersize= 0.5, linewidth=1, color ="red")
#    ax.plot(size,valMax, marker = ".", markersize= 0.5, linewidth=1, color ="red")
#     text = "fractal dimension N(r)=r^d\nd = [{:.3f} - {:.3f}] of cities".format( min(fractalDim),   max(fractalDim))
#    ax.text(0.05,0.05, text)
    plt.ylim([-.5,11])
    ax.legend()
    plt.savefig(pathOut)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
