#!/bin/bash

cd data

dirs=$(ls -d */)
for dir in $dirs; do
    dirname="${dir%/}"
    python3 regressionplot.py $dirname --regression-type linear 
    python3 regressionplot.py $dirname --regression-type exp 
    python3 regressionplot.py $dirname --regression-type log
done
cd ..
#done
