import time
import subprocess

#Change database connection settings
host = "localhost"
user = "root"
password = ""

#Get data
# start_time = time.time()
# print("Downloading TTC data...")
# p = subprocess.Popen(["python", "tod_extract.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# p.wait()
# out, err = p.communicate()
# if p.returncode != 0:
#     print(out)
#     print(err)
# print("Data downloaded in {} sec".format(time.time() - start_time))

input("Delete ttc-bus-delay-data-2019, sheet Apr 2019, column Incident ID: ")
input("Delete ttc-streetcar-delay-data-2019, sheet Apr 2019, column Incident ID: ")

#Create Database
start_time = time.time()
print("Creating database and tables")
p = subprocess.Popen(["python", "database_creation.py", host, user, password], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()
out, err = p.communicate()
if p.returncode != 0:
    print(out)
    print(err)
print("Database created in {} sec".format(time.time() - start_time))

#Populate tables

start_time = time.time()
print("Populating table bus_delay_data...")
p = subprocess.Popen(["python", "populate_table_bus_delay.py", host, user, password])
p.wait()
out, err = p.communicate()
if p.returncode != 0:
    print(out)
    print(err)
print("Tables populated in {} sec".format(time.time() - start_time))


start_time = time.time()
print("Populating table streetcar_delay_data...")
p = subprocess.Popen(["python", "populate_table_streetcar_delay.py", host, user, password])
p.wait()
out, err = p.communicate()
if p.returncode != 0:
    print(out)
    print(err)
print("Tables populated in {} sec".format(time.time() - start_time))

start_time = time.time()
print("Populating table subway_delay_data...")
p = subprocess.Popen(["python", "populate_table_subway_delay.py", host, user, password])
p.wait()
out, err = p.communicate()
if p.returncode != 0:
    print(out)
    print(err)
print("Tables populated in {} sec".format(time.time() - start_time))