import sqlite3 #import library

connection = sqlite3.connect('data.db') #initialise the connection, for url

cursor = connection.cursor() #allow to select and start things, cursor (run query and store the result)

create_table = "CREATE TABLE users (id int, username text, password text)" # create table
cursor.execute(create_table) #run query create_table

user = (1, ' desi', 'qwerty') # fill in the database
insert_query = "INSERT INTO users VALUES (?, ?, ?)" # insert the fill in
cursor.execute(insert_query, user) # run query user and insert_query

# new fill in database
users = [
    (2, 'fandi', 'qwer'),
    (3, 'ratno', 'aswd')
]
cursor.executemany(insert_query, users) # run query

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()