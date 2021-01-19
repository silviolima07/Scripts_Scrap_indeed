#!/bin/bash


cd /home/silvio/Web-Scrap-Selenium
#
./scrap_indeed.py  "Cientista de dados"
#
./scrap_indeed.py  "Analista de dados"
#
./scrap_indeed.py  "Engenheiro de machine learning"
#
./scrap_indeed.py  "Engenheiro de dados"

cd /home/silvio/Web-Scrap-Selenium/Streamlit/App-Indeed
date +'%d/%m/%Y %H:%M'> update


