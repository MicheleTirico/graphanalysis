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
import seaborn as sns
def main(args):
    pathIN, pathOUT, nameFile = args[0],args[1],args[2]
    patterns = ["holes", "mazes", "solitons", "movingSpots"]

    h = [ _ for _ in range (0,10)]
    df = pd.read_csv(pathIN, sep=";",header=None)
    df.insert(0,"p", df[0].astype(str))
    df["p"] =  df["p"].str.split("_").str[0]
    del df[21]
    data = []

    for i in range (0,4) :
        data.append(list(df[df["p"] == patterns[i]][2]))
    print (data)
    for i in range (0,len(data)):        plt.boxplot(data[i], positions=[0,1,2]) #, positions =[1,2,3])
#    plt.show()


    d1 = [[1, 2, 5], [5, 7, 2, 2, 5], [7, 2, 5, 4]]
    d2 = [[6, 4, 2], [1, 2, 5, 6, 2], [2, 3, 5, 1]]
    d3 = [[0, 4, 2], [1, 2,74, 6, 2], [2, 5, 1]]

    p1 = [-0.4,  1.6,  3.6]
    p2 = [0.4, 2.4, 4.4]
    n = .4
    s = 1
#    plt.boxplot(d2, positions =[1,2,3])
#    plt.boxplot(d2, positions =[1+n,2+n,3+n])
#    plt.boxplot(d3, positions =[1+n,2+n,3+n])

    plt.xticks([0,1,2,3], ["0","1","3","4"])
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
