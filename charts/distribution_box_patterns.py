"""
From a csv file we obtain a chart. The csv file contains a distribution for each line.
First of all, we compute the list of values of each row, then we compute the box of each column
in:     the path of the distribution (csv)
out:    the plot of the box plot
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main(args):
    pathIN, pathOUT, nameFile = args[0],args[1],args[2]
    print (pathIN)
    patterns = ["holes", "mazes", "solitons", "movingSpots"]
    for pattern in patterns:
        data = []
        print (pattern)
        for pos, line in enumerate(open(pathIN, "r")) :
            line = line.split(";")[0:-1]
            pattern_line = line [0]
            line = line[1:-1]
#            print(line)
            if pattern in pattern_line:
                a = [float(line[i]) for i in range(0,8)]
                del a[0]
                del a[1]
                print (a)
                data.append(a)

        m = np.matrix(data)
        t = m.getT()
        data = m
        fig, ax = plt.subplots()
        plt.ylim([-0.02,1])
        ax.set_title("degree distribution_"+pattern)
        ax.set_xlabel("degree k")
        ax.set_ylabel("probability p(k)")
        ax.set_xticklabels([1,3,4,5,6,7])
    #    ax.set_yticklabels([round(0.1*i,1) for i in range(-1,11)])
        ax.boxplot(data)
        plt.savefig(pathOUT + nameFile +"_"+pattern+".png")
        print ("png, go to ->",pathOUT)
#        plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])




    """
    if pos != 0 and pos != 1 and pos !=3 and pos <= 8:
        print(line)
        line =line[:-1]
        line = line.split(";")
        a = []
        for i in line :
            try :
                a.append (float(i))
            except:
                pass
                data.append(a)
                """
