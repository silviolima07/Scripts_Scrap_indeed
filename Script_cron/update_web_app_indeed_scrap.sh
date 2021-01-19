#!/bin/bash
cd /home/silvio/Web-Scrap-Selenium/Streamlit/App-Indeed
cp -r /home/silvio/Web-Scrap-Selenium/CSV/* CSV
git add .
git commit -m "Update CSV ->`date +'%d/%m/%Y %H:%M'`"
echo "Updating CSV file"
git push


