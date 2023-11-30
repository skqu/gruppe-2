import mysql.connector

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

#mycursor.execute("CREATE TABLE lommeregner_historik (calc VARCHAR(255))")

