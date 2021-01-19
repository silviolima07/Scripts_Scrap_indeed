#!/bin/bash

# Executar scrap dos cargos

cd /home/silvio/Web-Scrap-Selenium
#
./scrap_indeed.py  "Cientista de dados"
#

./scrap_indeed.py  "Analista de dados"
#
./scrap_indeed.py  "Engenheiro de machine learning"
#
./scrap_indeed.py  "Engenheiro de dados"

touch update-+`date +'%d/%m/%Y %H:%M'`

#Atualizar o web app


cd /home/silvio/Web-Scrap-Selenium/Streamlit/App-Indeed

cp -r /home/silvio/Web-Scrap-Selenium/CSV/* CSV

git add .
git commit -m "Update CSV ->`date +'%d/%m/%Y %H:%M'`"
echo "Updating CSV file"
git push

