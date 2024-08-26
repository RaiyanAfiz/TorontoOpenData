# Toronto Open Data Data Engineering Project

## An ETL project written in Python and using the pandas library!

This project is an exploration into the world of data engineering, mainly focusing on the practical implementation of ETL pipelines in Python. It also serves as hands-on experience using the pandas library to manipulate data and gain proficiency in working with Excel files from within Python.

### Key Features
* Downloads data from the toronto open data api.
* Processes and clean data to remove inconsistencies. 
* Loads the data into a database for further analysis. 
* Working with Excel inside of Python.



## Installation

You may use the [pip](https://pip.pypa.io/en/stable/) package manager to install the following Python libraries needed for this project.

```bash
pip install pandas
pip install openpyxl
pip install requests
pip install MySQL-connector-python
```
Note: You may need to use a different MySQL connector based on your environment. 

You also need a [MySQL](https://dev.mysql.com/downloads/) server instance running.



## Usage

Add the necessary credentials to [main.py](main.py) and [reset.py](reset.py) to connect to your database. 

```Python
host = "localhost"
user = "root"
password = "123456"
```
Note: Be careful with your credentials.

### [main.py](main.py)

Run once to have all the data stored in your database. 

### [reset.py](reset.py)

Uncomment and run as needed.



## To Do / Work in Progress

* Improved data consistency. 
    * Direction sometimes "N/W" vs "NW"
* Make the function of `CleanData()` into a Python module
* Multi-treaded data input



## License

This project is under the [MIT](https://choosealicense.com/licenses/mit/) license.

This data used in this project is used under the [Toronto Open Data](https://open.toronto.ca/open-data-license/) license.