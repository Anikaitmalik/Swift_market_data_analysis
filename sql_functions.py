# importing dependencies :

import os
import pandas as pd


import mysql.connector
from dotenv import load_dotenv

# loading credentials : 

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host= os.getenv("HOST")
database = "swiftmarket"

# establishing connection : 

connection = mysql.connector.connect(user = user,
                                     password = password,
                                     host = host,
                                     database = database)

cursor = connection.cursor()

# to read sql query :

def read_table(query):
    """ reading sql query.Only for select query"""
    """ returns onlu pd.DataFrame"""

    cursor.execute(query)
    rows = cursor.fetchall()
    return pd.DataFrame(data= rows , columns = cursor.column_names)

# to read the table_names and store in a list :

def read_table_names(query1):
    table_names = []
    cursor.execute(query1)
    rows = cursor.fetchall()
    for row in rows:
        table_names.append(row)
    return table_names