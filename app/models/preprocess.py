import os

from dotenv import load_dotenv

import mysql.connector
from mysql.connector import errorcode


load_dotenv()
MYSQL_CONFIG = {
    'user': os.getenv("rds_user"), 
    'password': os.getenv("rds_password"),
    'host': os.getenv("rds_host")
}

# Connecting to MySQL
try:
    cnx = mysql.connector.connect(**MYSQL_CONFIG)
except mysql.connector.Error as err:
    print(err)

else:
    print("Successfully connected to MySQL.")

cursor = cnx.cursor()


# Using/Creating database
DB_NAME = "wehelp_third"

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


# Creating tables
TABLES = {}

TABLES['messages'] = (
    "CREATE TABLE `messages` ("
    "  `id` bigint NOT NULL AUTO_INCREMENT,"
    "  `message` varchar(255),"
    "  `image_url` varchar(255),"
    "  PRIMARY KEY (`id`))")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


cnx.commit()

print("Closing")
cursor.close()
cnx.close()
