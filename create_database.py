import sqlite3
import config
import os

db_path = os.path.join(config.BASE_DIR, 'db', 'data.db')
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
cursor.execute("INSERT INTO users VALUES (1, 'desi', 'qwerty')")


create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()