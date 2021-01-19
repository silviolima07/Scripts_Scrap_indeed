#!/bin/bash

cd /home/silvio/Web-Scrap-Selenium
#
./scrap_indeed.py  "Cientista de dados"
#

if (($? == 0)); then
   echo "scrap ok"
else
   echo "Deu erro no scrap"
   exit 1
fi
