import sqlite3

# Connection
def create_connection(db_file):
    try:
        return sqlite3.connect(db_file)
    except:
        print("Connection Error: " + db_file)
