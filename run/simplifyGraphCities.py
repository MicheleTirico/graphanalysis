import sys
import os
import networkx as nx

# parameters
nameFolder = ".."
pathFolder = "../data/"+nameFolder
pathStore = "../data/cities_dgs"

os.mkdir(pathStore) # make folder to store dgs of cities

for city in os.listdir(pathFolder):
    city = str(city)
    print (city)
    pathGraph = pathFolder + "/"+city+"/edges/edges.shp"
    G=nx.read_shp(pathGraph,  simplify =  False, geom_attrs = False , strict = False)
    
