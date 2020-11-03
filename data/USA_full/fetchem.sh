#!/bin/sh

if [ ! -f area_titles.csv ]; then
    wget https://data.bls.gov/cew/doc/titles/area/area_titles.csv
fi

if [ ! -f 2017.annual.singlefile.csv ]; then
    https://data.bls.gov/cew/data/files/2017/csv/2017_annual_singlefile.zip
    unzip 2017_annual_singlefile.zip
fi
