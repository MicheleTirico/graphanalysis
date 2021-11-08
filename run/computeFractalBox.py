"""
given a set of graphs, the script compute the for each of them the csv of the number of boxes (with different size) needed to cover all vertices.
in:     the folder where is stored the graphs
out:    the folder where are stored the csv
"""
import sys
import os

def main(args):
    pathIN, pathOUT = args[0],args[1]
    print (pathIN)
    os.system("mkdir" + pathOUT)
    p = 0
    for name in os.listdir(pathIN):
        print(name, p )
        pathFileDgs = pathIN + name
        pathFileCsv = pathOUT + os.path.splitext(name)[0]
        os.system("java -cp ../jars/graphStreamAnalysis.jar fractalAnalysis.BoxCounting "+pathFileDgs + " " + pathFileCsv + ".csv true" )
        p+=1

if __name__ == "__main__":
    main(sys.argv[1:])
