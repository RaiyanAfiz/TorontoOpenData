import time
import subprocess

#Change database connection settings
host = "localhost"
user = "root"
password = ""

# start_time = time.time()
# print("Downloading TTC data...")
# p = subprocess.Popen(["python", "tod_extract.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# p.wait()
# out, err = p.communicate()
# if p.returncode != 0:
#     print(out)
#     print(err)
# print("Data downloaded in {} sec".format(time.time() - start_time))

start_time = time.time()
print("Creating database and tables")
p = subprocess.Popen(["python", "database_creation.py", host, user, password], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()
out, err = p.communicate()
if p.returncode != 0:
    print(out)
    print(err)
print("Database created in {} sec".format(time.time() - start_time))


start_time = time.time()
print("Populating tables")
p = subprocess.Popen(["python", "populate_table.py", host, user, password])
p.wait()
out, err = p.communicate()
if p.returncode != 0:
    print(out)
    print(err)
print("Tables populated in {} sec".format(time.time() - start_time))