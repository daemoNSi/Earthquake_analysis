import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='earthquake_analysis',
    autocommit=True
)

mycursor = db.cursor(buffered=True)

def tree_window(column_name, number_of_columns, table_name):
    window = tk.Tk()
    window.geometry('1200x1000')
    window.title('Data')

    tree = ttk.Treeview(window, columns=column_name,
                        show='headings', height=60)
    column_order = list()
    for number in range(1, number_of_columns+1):
        column_order.append(f'#{number}')

    for numb, name in zip(column_order, column_name):
        tree.column(numb, anchor=tk.W, width=150)
        tree.heading(numb, text=name)

    mycursor.execute(f'select * from {table_name}')
    for i in mycursor:
        tree.insert('', 'end', text='1', values=i)

    tree.pack()
    window.mainloop()


# def tree_window():
#     window = tk.Tk()
#     window.geometry('1200x1000')
#     window.title('Data')
#
#     tree = ttk.Treeview(window, columns=('time', 'latitude', 'longitude', 'depth',
#                                          'mag', 'magType', 'nst', 'gap', 'dmin',
#                                          'rms', 'net', 'id', 'updated', 'place',
#                                          'type', 'horizontalError', 'depthError',
#                                          'magError', 'magNst', 'status',
#                                          'locationSource', 'magSource'),
#                         show='headings', height=5)
#     column_order = list()
#     for number in range(1, 23):
#         column_order.append(f'#{number}')
#
#     column_names = ['time', 'latitude', 'longitude', 'depth',
#                     'mag', 'magType', 'nst', 'gap', 'dmin',
#                     'rms', 'net', 'id', 'updated', 'place',
#                     'type', 'horizontalError', 'depthError',
#                     'magError', 'magNst', 'status',
#                     'locationSource', 'magSource']
#
#     for numb, name in zip(column_order, column_names):
#         tree.column(numb, anchor=tk.W, width=85)
#         tree.heading(numb, text=name)
#
#     tree.pack()
#     window.mainloop()


# change time in the file from 2005-01-01T22:20:16.950Z ---> 2005-01-01 22:20:16
# import csv
# import re
# with open('earthquake_data.csv', 'r') as f:
#     csvreader = csv.reader(f, delimiter=',')
#     line_count = 0
#     header = ''
#     for row in csvreader:
#         if line_count == 0:
#             print(','.join(row))
#             line_count += 1
#         else:
#             strin = re.sub("T|.[0-9]+Z"," ", row[0])

# parse data from csv into tables
# def add_data_from_csv():
#     with open('earthquake_data.csv', 'r') as f:
#         csvreader = csv.reader(f, delimiter=',')
#         line_count = 0
#         header = ''
#         for row in csvreader:
#             if line_count == 0:
#                 print(','.join(row))
#                 line_count += 1
#             else:
#                 row_zero = re.sub("T|.[0-9]+Z"," ", row[0])
#                 row_twelve = re.sub("T|.[0-9]+Z"," ", row[12])
#                 mycursor.execute(f'INSERT INTO {tables[0]} (id,time,latitude,'
#                                  f'longitude,depth,mag,magType,place,'
#                                  f'locationSource,magSource) VALUES '
#                                  f'(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
#                                  (row[11],row_zero,row[1],row[2],row[3],row[4],row[5],row[13],row[20],row[21]))
#                 mycursor.execute(f'INSERT INTO {tables[1]} (eqid,nst,gap,dmin,rms,net,magNst) VALUES '
#                                  f'(%s,%s,%s,%s,%s,%s,%s)',
#                                  (row[11], row[6], row[7], row[8], row[9], row[10], row[18]))
#                 mycursor.execute(f'INSERT INTO {tables[2]} (erthqid,horizontalError,depthError,magError) VALUES '
#                                  f'(%s,%s,%s,%s)',
#                                  (row[11], row[15], row[16], row[17]))
#                 mycursor.execute(f'INSERT INTO {tables[3]} (otherid,updated,type,status) VALUES '
#                                  f'(%s,%s,%s,%s)',
#                                  (row[11], row_twelve, row[14], row[19]))
# add_data_from_csv()