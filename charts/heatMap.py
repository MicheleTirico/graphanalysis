"""
make a heatmap from dateset
in: dataset
out:png
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def main(args):
    pathIn, pathOut = args[0],args[1]
    print (pathIn, pathOut)

    df = pd.read_csv(pathIn,sep=",")
    del df["Unnamed: 11"]
    list_pc = list(set(list(df["pc"])))
    list_pr = list(set(list(df["pr"])))
    list_pc.sort()
    list_pr.sort()

    print (list_pc,list_pr,sep="\n")
    keys =list(df.keys()) [2:]
    print (keys)
#    keys = ["node"]
    for key in keys:
        dataKey = []
        for pc in list_pc:
            line = []
            for pr in list_pr:
                val = 0.0
                try:
                    val = (df.loc[(df['pc'] == pc ) & (df['pr'] == pr)][key])
                    line.append(float(val.values[0]))
            #        print (type(val))
            #        print(df.at(pc))
                except:
                    line.append(0.0)
#                    print(val)
            dataKey.append(line)    #    print(dataKey)
        mat = np.array(dataKey) #
        print (mat)



        fig, ax = plt.subplots()

        im = ax.imshow(mat)
        cbar = ax.figure.colorbar(im, ax=ax)
#        im, cbar = heatmap(mat, list_pc, list_pr, ax=ax,cmap="YlGn", cbarlabel=key)
#        texts = annotate_heatmap(im, valfmt="{x:.1f} t")

        fig.tight_layout()
        ax.set_xticks(np.arange(len(list_pc)))
        ax.set_yticks(np.arange(len(list_pr)))
        ax.set_xticklabels(list_pc)
        ax.set_yticklabels(list_pr)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
        rotation_mode="anchor")

#        plt.show()
        plt.savefig(pathOut+"_"+key+".png")


"""
fig, ax = plt.subplots()
"""
"""
        # We want to show all ticks...
        ax.set_xticks(np.arange(len(farmers)))
        ax.set_yticks(np.arange(len(vegetables)))
        # ... and label them with the respective list entries
        ax.set_xticklabels(farmers)
        ax.set_yticklabels(vegetables)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(vegetables)):
            for j in range(len(farmers)):
                text = ax.text(j, i, harvest[i, j],
                               ha="center", va="center", color="w")

        ax.set_title("Harvest of local farmers (in tons/year)")
        fig.tight_layout()
#            pcline = df.loc[df['pc'] == pc]
        #    if pcline["pr"]==p:
        #    print (pc,pr)
#            if float(pcline["pr"]) == float(pr):
#            if pcline['pr']== pr:

    data = []
    for pos, line in enumerate(open(pathIn, "r")) :
        print (line)


"""

























if __name__ == "__main__":
    main(sys.argv[1:])
