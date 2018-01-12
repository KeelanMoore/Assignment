# Normal Imports
import openpyxl
import sqlite3
import matplotlib.pyplot as plt

# Custom Imports
from easy_sql import *
from sql_tables import *
from easy_excel import *

# DB Setup
db_file = 'database.db'
connection = create_connection(db_file)
cursor = connection.cursor()

# Query  Aus State Temps
query_data = query_aus_state_temps(connection, cursor)

# Dict Format {[year, state] : [temp, n]}
new_data = {}
for values in query_data:
    year = values[0][:4]
    state = values[1]
    temp = values[2]
    if state in new_data:
        new_data[year, state][0] += temp
        new_data[year, state][1] += 1
    else:
        new_data[year, state] = [temp,1]

# Array Format [year, state, mean_temp]
state_means = []
for year_state in new_data:
    mean = new_data[year_state][0] / new_data[year_state][1]
    state_means.append([year_state[0], year_state[1], mean])
    
# Open Workbook
file_path = "World Temperature.xlsx"
workbook = open_workbook(file_path)
sheet = create_sheet(workbook, "Comparison")

# Fill Workbook
titles = ["Date", "Country", "Temperature"]
fill_sheet(sheet, titles, state_means)

# Save Workbook
file_path = "World Temperature.xlsx"
workbook.save(filename = file_path)

# Query Aus Date and Temps
cursor.execute("""SELECT date, av_temp
                  FROM country_table
                  WHERE country LIKE 'Australia'
                  AND av_temp is NOT NULL
                  ORDER BY date""")
data = cursor.fetchall()
    
        
# Graph
plt.title("Difference Between State and National Temperatures")
plt.xlabel("Year")
plt.ylabel("Temperature Difference")
plt.show()
