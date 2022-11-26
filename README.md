# CSV to Chart

An easy bar and pie charts generator base on a CSV file.
It could be performed through the web browser or the command line.

Installation:
You need to clone into your local repository and start the virtual enviromental as follow:
	'git clone git@github.com:vanyegv/General-API-for-CSV-Files.git
	cd General-API-for-CSV-Files && source env/bin/activate
	pip3 -r requirements.txt'

Once dowloaded and started virtual enviroment with all dependencies, you have two option to execute the program through the web browser or through the command line: 

	'uvicorn main:app --reload
	https://127.0.0.1:800/api'

	'https://127.0.0.1:800/api?path=path_to_csv'

	'python3 main.py'

	'python3 main.py path_to_csv'
