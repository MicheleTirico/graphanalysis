"""
simplify a list of graphs
in:     the path of in files
out:    the path of outputs
"""

import sys
import os

def main(args):
    pathIN, pathOUT = args[0],args[1]
    print (pathIN, pathOUT)

    os.system("mkdir" + pathOUT)
    for name in os.listdir(pathIN):
        print(name)
        pathFileDgs = pathIN + name
        os.system("java -cp ../jars/simplifynetwork.jar simplifynetwork.Simplifier "+pathFileDgs + " " + pathOUT+name)

if __name__ == "__main__":
    main(sys.argv[1:])
