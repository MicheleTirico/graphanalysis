
"""
get the fractal dimension (png) of all cities
in:     csv, each row is a file
out:    png log-log
"""

import math as mt
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main(args):
    pathIN, nameFile = args[0],args[1]
    print (pathIN, nameFile)
    fig, ax = plt.subplots()
    ax.set_title("fractal dimension")
    ax.set_ylabel("log of number of not empty boxes (N(r))")
    ax.set_xlabel("log of number of boxes (r)")
    valMin , valMax = [100 for i in range (1000)] , [0 for i in range (1000)]
    fractalDim = []
    all = []
    for file in os.listdir(pathIN):
        if "csv" and "fractal" in str(file) and "png" not in str(file):
            print(file)
            data = pd.read_csv(pathIN +file,sep=";")
            v = list(data["val"])
            all.append(v)
    # print (len(all))


    for p, line in enumerate(all) :
    #     print(line)
#        line = line.split(",")
#        city = line[0]
        minBox = 1
        val = line[minBox:]
        val = [float(i) for i in val]
        size = [i for i in range(1,len(val)+1) ]
        val = [mt.log(i) for i in val]
        size = [mt.log(i) for i in size]
        m,b = np.polyfit(size,val,1)
        fractalDim.append(m)
#        print (city,m,b)
        i = 0
        while i < len (val) :
            if val[i] <= valMin[i]:  valMin[i] = val[i]
            if val[i] >= valMax[i]: valMax[i] = val[i]
            i+=1
        valMin, valMax = valMin[0:len(val)], valMax[0:len(val)]
        ax.plot(size,val, marker = ".", markersize= 0.5, linewidth=0.5, color="silver")

    fractalDim = [abs(i) for i in fractalDim]
    ax.plot(size,valMin, marker = ".", markersize= 0.5, linewidth=1, color ="red")
    ax.plot(size,valMax, marker = ".", markersize= 0.5, linewidth=1, color ="red")
    text = "fractal dimension N(r)=r^d \nd = [{:.3f} - {:.3f}]".format( min(fractalDim),   max(fractalDim))
    ax.text(0.05,0.05, text)
#    ax.set_yticklabels([round(i,1) for i in range(0,10)])
    plt.ylim([-.5,10])
    plt.savefig(pathIN+nameFile+".png")
#    plt.show()
    print ("png, go to ->",pathIN+nameFile+".png")


if __name__ == "__main__":
    main(sys.argv[1:])
