"""
create the fractal dimension of a list of networks
in: list of DGS
out:png
"""
import sys
import os

def main(args):
    print("parameters: \n0 -> pathIn \n1 -> pathOut to store csv of fractal \n2 -> path out to store the png")
    pathIN, pathOUT, pathOUTpng = args[0],args[1],args[2]
    os.system("mkdir " + pathOUT)
    terJava = "java -cp {} {} {} {}".format("../jars/graphStreamAnalysis.jar", "run.BoxCounting_list", pathIN,pathOUT)
    os.system(terJava)
#    terChart = "python3 {} {} {}".format("../charts/fractal_all.py",pathOUT, pathOUTpng)
    terChart = "python3 {} {} {}".format("../charts/fractal_list.py",pathOUT, pathOUTpng)
    os.system(terChart)

if __name__ == "__main__":
    main(sys.argv[1:])
