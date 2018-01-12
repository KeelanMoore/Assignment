# Normal Imports
import sqlite3

# Custome Imports
from easy_sql import *
from sql_tables import *

# DB Setup
db_file = 'database.db'
connection = create_connection(db_file)
cursor = connection.cursor()

# Create Tables
create_southern_cities_table(cursor)

cursor.execute("""SELECT DISTINCT city, country, latitude, longitude
                  FROM city_table
                  WHERE latitude LIKE '%S'
                  ORDER BY country""")

data = cursor.fetchall()

for values in data:
    print(values)
    #fill_southern_cities_table(connection, cursor, values)

cursor.execute("""SELECT av_temp
                  FROM state_table
                  WHERE state LIKE 'Queensland' and av_temp is NOT NULL""")

data = cursor.fetchall()

n = 0
average = 0
maximum = 0
minimum = 1000
for value in data:
    n += 1
    average += value[0]
    if value[0] < minimum: minimum = value[0]
    if value[0] > maximum: maximum = value[0]

print("Average", average / n)
print("Minimum", minimum)
print("Maximum", maximum)

#connection.commit()
