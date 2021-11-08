"""
create a chart with selected, explore and cities fractal.
in: csv cities, explored, selected
out:png
"""
import sys
import os
import math as mt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sys.path.append("../tools")

from tools import *

def main(args):
    print("parameters: \n0 -> pathInCities \n1 -> pathInExplore \n2 -> pathInSelected \n3 -> pathOut to store the png")
    pathInCities, pathInExplore, pathInSelected, pathOut = args[0],args[1],args[2],args[3]
    os.system("mkdir " + pathOut)

    fig, ax = plt.subplots()
#    ax.set_title("fractal dimension")
    ax.set_ylabel("log of number of not empty boxes (N(r))")
    ax.set_xlabel("log of number of boxes (r)")
    patterns = ["holes", "mazes", "solitons", "movingSpots"]
    colors = ["red", "green","blue","purple"]

    valMin , valMax = [100 for i in range (1000)] , [0 for i in range (1000)]

    # cities
    dim = []
    data = []
    for file in os.listdir(pathInCities):
        if "csv"  in str(file): #    print(file)
    #        data = pd.read_csv(pathInCities +file,sep=";")
            data.append(list(pd.read_csv(pathInCities +file,sep=";")["val"]))
    for p, line in enumerate(data) :    #     print(line)
        val = line[1:] # min box = 1
        val = [float(i) for i in val]
        size = [i for i in range(1,len(val)+1) ]
        val = [mt.log(i) for i in val]
        size = [mt.log(i) for i in size]
        m,b = np.polyfit(size,val,1)
        dim.append(m)
        i = 0
        while i < len (val) :
            if val[i] <= valMin[i]:  valMin[i] = val[i]
            if val[i] >= valMax[i]: valMax[i] = val[i]
            i+=1
        valMin, valMax = valMin[0:len(val)], valMax[0:len(val)]
    sizeMinRem, valMinRem = listRem(size,valMin)
    sizeMaxRem, valMaxRem = listRem(size,valMax)
    ax.fill_between(sizeMaxRem, valMaxRem,   color ="#DCDCDC",label="cities (d=[{:.3f} - {:.3f}])".format( abs(min(dim)),   abs(max(dim)))) # "#5f5f5f")
    ax.fill_between(sizeMinRem, valMinRem,   color ="white",) # "#5f5f5f")



    # explore
    dim = []
    data = []
    for file in os.listdir(pathInExplore):
        if "fractal.csv"  in str(file) :# print(file)
    #        data = pd.read_csv(pathInCities +file,sep=";")
            data.append(list(pd.read_csv(pathInExplore +file,sep=";")["val"]))
    for p, line in enumerate(data) :    #     print(line)
        val = line[1:] # min box = 1
        val = [float(i) for i in val]
        size = [i for i in range(1,len(val)+1) ]
        val = [mt.log(i) for i in val]
        size = [mt.log(i) for i in size]
        m,b = np.polyfit(size,val,1)
        dim.append(m)
        i = 0
        while i < len (val) :
            if val[i] <= valMin[i]:  valMin[i] = val[i]
            if val[i] >= valMax[i]: valMax[i] = val[i]
            i+=1
        valMin, valMax = valMin[0:len(val)], valMax[0:len(val)]
    sizeMinRem, valMinRem = listRem(size,valMin)
    sizeMaxRem, valMaxRem = listRem(size,valMax)
    ax.fill_between(sizeMaxRem, valMaxRem, color="none", hatch="///", edgecolor="gray", linewidth=0.01,label="explore (d=[{:.3f} - {:.3f}])".format( abs(min(dim)),   abs(max(dim))) ) # "#5f5f5f")
#    ax.fill_between(sizeMaxRem, valMaxRem,  hatch="///", alpha=0.5, linewidth=0.5, color ="black",label="explore (d=[{:.3f} - {:.3f}])".format( abs(min(dim)),   abs(max(dim))) ) # "#5f5f5f")
    ax.fill_between(sizeMinRem, valMinRem, color ="white") # "#5f5f5f")

    # selected
    dim=[]
    for file in os.listdir(pathInSelected):
        if "fractal.csv"  in str(file) :#
            print(file)
            pattern = getPattern(str(file))
            data = pd.read_csv(pathInSelected +file,sep=";")
            v = list(data["val"])
            minBox = 1
            val = v[minBox:]
            val = [float(i) for i in val]
            size = [i for i in range(1,len(val)+1) ]
            val = [mt.log(i) for i in val]
            size = [mt.log(i) for i in size]
            m,b = np.polyfit(size,val,1)
            dim.append(abs(m))
            size, val= listRem(size,val)
            ax.plot(size,val, marker = ".", markersize= 5, linewidth=.0,label=str(pattern)+" (d="+"{:.3f}".format(abs(m)) +")")


    plt.legend(prop={'size': 9})
#    plt.show()
    plt.savefig(pathOut)
if __name__ == "__main__":
    main(sys.argv[1:])
