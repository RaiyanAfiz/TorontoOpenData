import mysql.connector
import sys

db = mysql.connector.connect(
    host= sys.argv[1],
    user= sys.argv[2],
    passwd= sys.argv[3]
)

myCursor = db.cursor()
db_name = "toronto_open_data"


#Create database
myCursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
myCursor.execute("USE {}".format(db_name))

#Create tables
tables = ["ttc_bus_delay_data", "ttc_streetcar_delay_data", "ttc_subway_delay_data"]

myCursor.execute('''
                    CREATE TABLE IF NOT EXISTS {}
                    (
                        incident_id INT NOT NULL AUTO_INCREMENT, 
                        date DATE,
                        route VARCHAR(255),
                        time TIME,
                        day CHAR(10),
                        location VARCHAR(255),
                        incident VARCHAR(255),
                        min_delay INT,
                        min_gap INT,
                        direction VARCHAR(255),
                        vehicle INT,
                        PRIMARY KEY(incident_id)
                    )
                '''.format(tables[0]))

myCursor.execute('''
                    CREATE TABLE IF NOT EXISTS {}
                    (
                        incident_id INT NOT NULL AUTO_INCREMENT, 
                        date DATE,
                        route VARCHAR(255),
                        time TIME,
                        day CHAR(10),
                        location VARCHAR(255),
                        incident VARCHAR(255),
                        min_delay INT,
                        min_gap INT,
                        direction VARCHAR(255),
                        vehicle INT,
                        PRIMARY KEY(incident_id)
                    )
                '''.format(tables[1]))

myCursor.execute('''
                    CREATE TABLE IF NOT EXISTS {}
                    (
                        incident_id INT NOT NULL AUTO_INCREMENT, 
                        date DATE,
                        time TIME,
                        day CHAR(10),
                        station VARCHAR(255),
                        delay_code CHAR(15),
                        min_delay INT,
                        min_gap INT,
                        bound CHAR(10),
                        line VARCHAR(255),
                        vehicle INT,
                        PRIMARY KEY(incident_id)
                    )
                '''.format(tables[2]))


tables = ["bus_delay_data_dict", "streetcar_delay_data_dict", "subway_delay_data_dict"]
for table in tables:
    myCursor.execute('''
                        CREATE TABLE IF NOT EXISTS {}
                        (
                            field_name CHAR(15),
                            description VARCHAR(10000),
                            example CHAR(50),
                            PRIMARY KEY(field_name)
                        )
                    '''.format(table))

myCursor.execute('''
                    CREATE TABLE IF NOT EXISTS {}
                    (
                        sub_code CHAR(15),
                        description VARCHAR(255),
                        PRIMARY KEY(sub_code)
                    )
                '''.format("sub_code"))


#Close Connections
db.commit()
db.close()