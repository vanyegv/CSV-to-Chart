# CSV to Chart

An easy bar and pie charts generator base on a CSV file.
It could be performed through the web browser or the command line.

Installation:
git clone git@github.com:vanyegv/General-API-for-CSV-Files.git
cd General-API-for-CSV-Files && source env/bin/activate
pip3 -r requirements.txt

uvicorn main:app --reload
https://127.0.0.1:800/api

https://127.0.0.1:800/api?path=path_to_csv

python3 main.py

python3 main.py path_to_csv