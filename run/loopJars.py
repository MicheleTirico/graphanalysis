
"""
execute the jar for a set of files in a folder
input : jar and directory
output: compute the jar
"""
import sys
import os

def main(args):
    jar = args[0]
    nameClass = args[1]
    directory = args[2]
    # for file in folder: execute the jar
    for filename in os.listdir(directory):
        os.system("java -cp ",jar,nameClass,directory+"/"+filename)


if __name__ == "__main__":
    main(sys.argv[1:])
