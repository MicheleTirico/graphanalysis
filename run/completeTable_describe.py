"""
create the table of indicators
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
    os.system( "java -cp {} {} {} {}".format("../jars/graphStreamAnalysis.jar", "run.CreateTable", pathIN,pathOUT+nameFile+"_all.csv"))
    os.system( "python3 {} {} {} {}".format("createTable_describe.py",pathOUT+nameFile+"_all.csv",pathOUT, nameFile+"_describe"))
    os.system( "python3 {} {} {} {}".format("createTable_dense.py",pathOUT+nameFile+"_all.csv",pathOUT, nameFile+"_dense"))




if __name__ == "__main__":
    main(sys.argv[1:])

"""
steps:
create csv with degreeDistribution (java)
create chart (py)
"""
