import csv
import mysql.connector
import tkinter as tk
from tkinter import ttk
import re
# from TreeView import tree_window
from table_view import create_table

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='earthquake_analysis',
    autocommit=True
)

mycursor = db.cursor(buffered=True)

tables = ['Earthquakes', 'Seismic_station_data', 'Errors', 'Other_data']
db_name = 'earthquake_analysis'

# mycursor.execute(f'ALTER TABLE {tables[1]} CHANGE COLUMN dmin dmin varchar(7) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[1]} CHANGE COLUMN magNst magNst varchar(7) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[2]} CHANGE COLUMN horizontalError horizontalError varchar(7) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[2]} CHANGE COLUMN depthError depthError varchar(7) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[2]} CHANGE COLUMN magError magError varchar(7) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[1]} CHANGE COLUMN rms rms DOUBLE DEFAULT 0')

# mycursor.execute(f'ALTER TABLE {tables[1]} CHANGE COLUMN nst nst varchar(32) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[1]} CHANGE COLUMN gap gap varchar(32) DEFAULT ""')
# mycursor.execute(f'ALTER TABLE {tables[1]} CHANGE COLUMN rms rms varchar(32) DEFAULT ""')

def check_rows(table):
    mycursor.execute(f'SELECT * from {table}')
    return mycursor.rowcount


def table_exists():
    try:
        mycursor.execute(f"CREATE TABLE {tables[0]} (id varchar(15) PRIMARY KEY,"
                         "time DATETIME, latitude FLOAT, longitude FLOAT, depth FLOAT, mag FLOAT,"
                         "magType varchar(5), place varchar(50),locationSource varchar(5),"
                         "magSource varchar(5))")
        print(f'Table - {tables[0]} has been created')
    except:
        print(f'Table - {tables[0]} already exists')
    try:
        mycursor.execute(f"CREATE TABLE {tables[1]} (eqid varchar(15) PRIMARY KEY,"
                         f"FOREIGN KEY(eqid) REFERENCES {tables[0]} (id),"
                         "nst varchar(32) DEFAULT "",gap varchar(32) DEFAULT "",dmin varchar(7) DEFAULT "","
                         "rms varchar(32) DEFAULT "",net varchar(5),magNst varchar(7) DEFAULT "")")
        print(f'Table - {tables[1]} has been created')
    except:
        print(f'Table - {tables[1]} already exists')

    try:
        mycursor.execute(f"CREATE TABLE {tables[2]} (erthqid varchar(15) PRIMARY KEY,"
                         f"FOREIGN KEY(erthqid) REFERENCES {tables[0]} (id),"
                         "horizontalError varchar(7) DEFAULT "","
                         "depthError varchar(7) DEFAULT "",magError varchar(7) DEFAULT "")")
        print(f'Table - {tables[2]} has been created')
    except:
        print(f'Table - {tables[2]} already exists')

    try:
        mycursor.execute(f"CREATE TABLE {tables[3]} (otherid varchar(15) PRIMARY KEY,"
                         f"FOREIGN KEY(otherid) REFERENCES {tables[0]} (id),"
                         "updated DATETIME,type varchar(15), status varchar(15))")
        print(f'Table - {tables[3]} has been created')
    except:
        print(f'Table - {tables[3]} already exists')

    for table in tables:
        row_count = check_rows(table)
        if row_count == 0:
            print(f'{table} has 0 rows')

def show_tables():
    mycursor.execute('show tables from earthquake_analysis')
    for i in mycursor:
        print(i[0])

def describe_table(table):
    mycursor.execute(f'describe {table}')
    for i in mycursor:
        print(i)


headers = []
def get_headers(table):
    global headers
    mycursor.execute(f'describe {table}')
    for column_name in mycursor:
        headers.append(column_name[0])

get_headers(f'{tables[0]}')
# tree_window(headers, len(headers), tables[0])
create_table(headers, check_rows(tables[0]), tables[0])
