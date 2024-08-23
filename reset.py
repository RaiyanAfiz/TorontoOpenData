import mysql.connector
import sys

db = mysql.connector.connect(
    host= sys.argv[1],
    user= sys.argv[2],
    passwd= sys.argv[3]
)