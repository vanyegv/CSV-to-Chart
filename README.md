# **csv2chart**

An easy bar and pie charts generator base on a CSV file.
It could be performed through the web browser or the command line.

**Installation:**

You need to clone into your local repository and start the virtual enviromental as follow:

	git clone git@github.com:vanyegv/csv2chart.git
	cd General-API-for-CSV-Files && python3 -m venv env
	source env/bin/activate
	pip3 install -r requirements.txt

**Usage:**

Once dowloaded and started virtual enviroment with all dependencies, you have two option to execute the program through the web browser or through the command line:
+ To execute through the web browser execute as follow to start the server service:

	``uvicorn main:app --reload``

Now, the server is running, open your web browser and type the following URL:

	https://127.0.0.1:800/api?path=path_to_csv

If you don`t indicate the csv file, a default example data will be uploaded.

+ To execute throught the command line, you can execute as follow:

	``python3 main.py path_to_csv head_identifier head_values``

if you don`t declare heads, you will be redirected to a menu to choose the ones that you require.

	python3 main.py path_to_csv

If you don`t declare a csv file, an example data information will be displayed

	python3 main.py

*Screenshots*

	![Example from API] (/screenshoot1.png)


	![Example from terminal] (/screenshoot1.png)

