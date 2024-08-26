import shutil
import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= ""
)

myCursor = db.cursor()
db_name = "toronto_open_data"


# #Drop Database
# myCursor.execute("DROP DATABASE IF EXISTS {}".format(db_name))


# # #Drop Individual Tables
# myCursor.execute("USE {}".format(db_name))
# myCursor.execute("DROP Table IF EXISTS ttc_bus_delay_data")
# myCursor.execute("DROP Table IF EXISTS ttc_streetcar_delay_data")
# myCursor.execute("DROP Table IF EXISTS ttc_subway_delay_data")
# myCursor.execute("DROP Table IF EXISTS bus_delay_data_dict")
# myCursor.execute("DROP Table IF EXISTS streetcar_delay_data_dict")
# myCursor.execute("DROP Table IF EXISTS subway_delay_data_dict")
# myCursor.execute("DROP Table IF EXISTS sub_code")

# #Delete downloaded files
# shutil.rmtree("ttc_bus_delay_data")
# shutil.rmtree("ttc_streetcar_delay_data")
# shutil.rmtree("ttc_subway_delay_data")


#Close Connections
db.commit()
db.close()