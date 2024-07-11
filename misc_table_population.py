import mysql.connector
import pandas as pd
import re
import os
import sys

db = mysql.connector.connect(
    host= sys.argv[1],
    user= sys.argv[2],
    passwd= sys.argv[3]
)

myCursor = db.cursor()
db_name = "toronto_open_data"
tables = ["bus_delay_data_dict", "streetcar_delay_data_dict", "subway_delay_data_dict"]
folders = ["ttc_bus_delay_data", "ttc_streetcar_delay_data", "ttc_subway_delay_data"]
myCursor.execute("USE {}".format(db_name))

#Insert Excel File Data

for i in range(3):
    files = os.listdir(folders[i])

    for file in files:
        
        if re.search("-readme", file):
            file_path = os.path.join(folders[i], file)
            df = pd.read_excel(file_path)

            for j, row in df.iterrows():
                record = list(row)
                
                # insert table data
                sqlQuery = '''
                            INSERT INTO {} 
                            (field_name, description, example) 
                            VALUES ("{}", "{}", "{}")
                        '''.format(tables[i], *record)
                # Print sequentially according to the loop
                sqlQuery = sqlQuery.replace('\"nan\"', 'null').replace('nan', 'null')

                try:
                    myCursor.execute(sqlQuery)
                except Exception as e:
                    print(record)
                    print(e)
                    exit()


#Clean data for subway codes
df = pd.read_excel('ttc_subway_delay_data\\ttc-subway-delay-codes.xlsx')
cols = [0, 1, 4, 5]
df.drop(df.columns[cols], axis=1, inplace=True)
df.drop(0, inplace=True)
df1 = df.iloc[:, 0:2]
df2 = df.iloc[:, 2:4]
df1.columns = ['sub_code', 'description']
df2.columns = ['sub_code', 'description']
df3 = pd.concat([df1, df2])
df3.dropna(how='any',axis=0, inplace=True) 

for i, row in df3.iterrows():
    record = list(row)

    # insert table data
    sqlQuery = '''
                INSERT INTO sub_code
                (sub_code, description) 
                VALUES ("{}", "{}")
            '''.format(*record)
    # Print sequentially according to the loop
    sqlQuery = sqlQuery.replace('\"nan\"', 'null').replace('nan', 'null')

    try:
        myCursor.execute(sqlQuery)
    except Exception as e:
        print(record)
        print(e)
        exit()


#Close Connections
myCursor.close()
db.commit()
db.close()
