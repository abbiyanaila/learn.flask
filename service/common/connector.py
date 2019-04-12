import sqlite3
import os

base_path = os.getcwd()
db_path = os.path.join(base_path, 'db', 'data.db')

# connection = sqlite3.connect(db_path)
# cursor = connection.cursor()

def get_connection():
    return sqlite3.connect(db_path)

def get_cursor():
    return get_connection().cursor()