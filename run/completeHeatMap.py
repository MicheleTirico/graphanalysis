"""
create heatMap
in: list of DGS
out:csv
"""
import sys
import os

def main(args):
    print("parameters: \n0 -> pathIn \n1 -> pathOut \n2 -> name file")
    pathIN, pathOUT, nameFile = args[0],args[1],args[2]
    print (pathIN)
    os.system("mkdir" + pathOUT)
    terJava = "java -cp {} {} {} {}".format("../jars/graphStreamAnalysis.jar", "run.CreateTable_pcpr", pathIN,pathOUT+nameFile+".csv")
    os.system(terJava)
    terChart = "python3 {} {} {}".format("../charts/heatMap.py",pathOUT+nameFile+".csv",pathOUT+nameFile)
    os.system(terChart)



if __name__ == "__main__":
    main(sys.argv[1:])
