import mysql.connector
import csv

from mysql.connector import cursor

file_path = "data.csv"
config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "tema3.5"
}

mydb = mysql.connector.connect(
    host = config["host"],
    user = config["user"],
    password = config["password"],
    database = config["database"]
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE lommeregner_historik (calc int(255))")


csv_data = csv.reader(open('C:\\Users\\name\\OneDrive - IBA Erhvervsakademi Kolding\gruppe-2\data.csv'))
header = next(csv_data)


for row in csv_data:
    print(row)
    mycursor.execute("INSERT INTO lommeregner_historik (calc) VALUES (%s)", row)

mydb.commit()
mydb.close()