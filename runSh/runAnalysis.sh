#!/bin/bash

pathIn="../../rwrd/data/explore/exp_03/"
pathOut="../data/explore/exp_04/"
nameFile="explore"
mkdir $pathOut
java -cp ../graphStreamAnalysis/dist/graphStreamAnalysis.jar run.GetImages_list $pathIn $pathOut .1 1 black black false false
python3 ../run/completeDegree.py $pathIn $pathOut $nameFile"_degree"
python3 ../run/completeFractal.py $pathIn $pathOut $nameFile"_fractal"
python3 ../run/completeTable.py $pathIn $pathOut $nameFile"_table"
#python3 ../run/completeTable.py $pathIn $pathOut $nameFile"_table_list"
python3 ../run/completeHeatMap.py $pathIn $pathOut $nameFile"_heatmap"

echo "finish, go to "$pathOut
