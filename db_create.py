# Normal Imports
import sqlite3
import openpyxl

# Custom Imports
from easy_sql import *
from sql_tables import *
from easy_excel import *

# DB Setup
db_file = 'database.db'
connection = create_connection(db_file)
cursor = connection.cursor()

# Create Tables
create_country_table(cursor)
create_city_table(cursor)
create_state_table(cursor)

# Fill Tables
n = 0
country_file = 'GlobalLandTemperaturesByCountry.xlsx'
city_file = 'GlobalLandTemperaturesByMajorCity.xlsx'
state_file = 'GlobalLandTemperaturesByState.xlsx'
excel_paths = [country_file, city_file, state_file]

for path in excel_paths:
    n += 1
    workbook = open_workbook(path)
    sheet = open_sheet(workbook, 0)
    data = get_data(sheet)
    if n == 1: fill_country_table(connection, cursor, data)
    elif n == 2: fill_city_table(connection, cursor, data)
    elif n == 3: fill_state_table(connection, cursor, data)
    connection.commit()

cursor.close()
connection.close()
