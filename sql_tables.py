import sqlite3

# Create Table Functions
def create_country_table(cursor):
    command  = """CREATE TABLE IF NOT EXISTS country_table (
                  date TEXT NOT NULL,
                  av_temp REAL,
                  av_uncert REAL,
                  country TEXT NOT NULL);"""
    cursor.execute(command)

def create_city_table(cursor):
    command  = """CREATE TABLE IF NOT EXISTS city_table (
                  date TEXT NOT NULL,
                  av_temp REAL,
                  av_uncert REAL,
                  city TEXT NOT NULL,
                  country TEXT NOT NULL,
                  latitude TEXT NOT NULL,
                  longitude TEXT NOT NULL);"""
    cursor.execute(command)

def create_state_table(cursor):
    command  = """CREATE TABLE IF NOT EXISTS state_table (
                  date TEXT NOT NULL,
                  av_temp REAL,
                  av_uncert REAL,
                  state TEXT NOT NULL,
                  country TEXT NOT NULL);"""
    cursor.execute(command)

def create_southern_cities_table(cursor):
    command  = """CREATE TABLE IF NOT EXISTS southern_cities (
                  city TEXT NOT NULL,
                  country TEXT NOT NULL,
                  latitude TEXT NOT NULL,
                  longitude TEXT NOT NULL);"""
    cursor.execute(command)

# Fill Table Functions
def fill_country_table(connection, cursor, values):
    cursor.executemany("""INSERT INTO country_table (
                          date, av_temp, av_uncert, country)
                          VALUES (?, ?, ?, ?)""", (values))
    

def fill_city_table(connection, cursor, values):
    cursor.executemany("""INSERT INTO city_table (
                          date, av_temp, av_uncert, city,
                          country, latitude, longitude)
                          VALUES (?, ?, ?, ?, ?, ? ,?)""", (values))

def fill_state_table(connection, cursor, values):
    cursor.executemany("""INSERT INTO state_table (
                          date, av_temp, av_uncert, state, country)
                          VALUES (?, ?, ?, ?, ?)""", (values))

def fill_southern_cities_table(connection, cursor, values):
    cursor.executemany("""INSERT INTO southern_cities (
                          city, country, latitude, longitude)
                          VALUES (?, ?, ?, ?)""", (values))

# Query Table Functions
def query_aus_state_temps(connection, cursor):
    cursor.execute("""SELECT date, state, av_temp
                      FROM state_table
                      WHERE country LIKE 'Australia'
                      AND av_temp is NOT NULL
                      ORDER BY date, state""")
    return cursor.fetchall()
    
