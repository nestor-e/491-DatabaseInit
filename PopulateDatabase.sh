#!/bin/bash

python3 MySqlLoadFileFormater.py

USRN="guest"
HN="127.0.0.1"
echo $USRN
cat initDB.txt | mysql --host=$HN -u guest
