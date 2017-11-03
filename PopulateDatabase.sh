#!/bin/bash

python3 MySqlLoadFileFormater.py

USRN=$2
PW=$3
HN=$1

mysql --host=$HN --user=$USRN -p$PW < purgeDB.txt
mysql --host=$HN --user=$USRN -p$PW --local-infile < initDB.txt
