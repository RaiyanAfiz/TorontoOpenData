import mysql.connector
import pandas as pd
import re
import os
import sys

def CleanData():
    record[0] = str(record[0]).replace('00:00:00', '').strip()
    record[1] = str(record[1])
    record[2] = str(record[2])
    record[4] = str(record[4]).replace('\\', '-').replace('\"', '\'')
    record[8] = str(record[8]).replace('\\', '-').replace('\"', '\'')


db = mysql.connector.connect(
    host= sys.argv[1],
    user= sys.argv[2],
    passwd= sys.argv[3]
)

myCursor = db.cursor()
db_name = "toronto_open_data"
table = "ttc_bus_delay_data"
myCursor.execute("USE {}".format(db_name))

#Insert Excel File Data
files = os.listdir(table)

for file in files:
    
    if re.search("-readme", file) or re.search(".json", file):
        continue
    else:
        file_path = os.path.join(table, file)
        df_excel = pd.read_excel(file_path, sheet_name=None)

        for sheet_name, df in df_excel.items():
            if df.empty:
                continue

            try:
                df.drop("Incident ID", axis=1, inplace=True)
            except Exception as e:
                ''

            for i, row in df.iterrows():
                record = list(row)
                CleanData()
                
                
                # insert table data
                sqlQuery = '''
                            INSERT INTO {} 
                            (date, route, time, day, location, incident, min_delay, min_gap, direction, vehicle) 
                            VALUES ("{}", "{}", "{}", "{}", "{}", "{}", {}, {}, "{}", {})
                        '''.format(table, *record)
                # Print sequentially according to the loop
                sqlQuery = sqlQuery.replace('\"nan\"', 'null').replace('nan', 'null')

                try:
                    myCursor.execute(sqlQuery)
                except Exception as e:
                    print("File: {}, sheet: {}, line: {} ".format(file, sheet_name, i) + sqlQuery)
                    print(record)
                    print(e)
                    exit()


#Close Connections
myCursor.close()
db.commit()
db.close()
