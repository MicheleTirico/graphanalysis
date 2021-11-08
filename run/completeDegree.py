"""
create the degree distribution of a list of Files
in: list of DGS
out:png
"""
import sys
import os

def main(args):
    print("parameters: \n0 -> pathIn \n1 -> pathOut \n2 -> name file")
    pathIN, pathOUT, nameFile = args[0],args[1],args[2]
    print (pathIN)
    os.system("mkdir" + pathOUT)
    os.system("java -cp {} {} {} {}".format("../jars/graphStreamAnalysis.jar", "run.ComputeDistributionDegree", pathIN,pathOUT+nameFile+".csv"))
    os.system("python3 {} {} {}".format("../charts/distribution_box.py",pathOUT+nameFile+".csv",pathOUT+nameFile+".png"))
    os.system("python3 {} {} {} {}".format("../charts/distribution_box_patterns.py",pathOUT+nameFile+".csv",pathOUT, nameFile))
    os.system("python3 {} {} {} {}".format("../charts/distribution_box_patterns_merge.py",pathOUT+nameFile+".csv",pathOUT, nameFile))


if __name__ == "__main__":
    main(sys.argv[1:])
