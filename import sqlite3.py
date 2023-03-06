import sqlite3

# connect to the database
conn = sqlite3.connect('mydatabase.db')

# create a table
conn.execute('''CREATE TABLE users
             (id INT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL);''')

# insert some data into the table
conn.execute("INSERT INTO users (id, name, email, password) VALUES (1, 'Alice', 'alice@example.com', 'password123')")
conn.execute("INSERT INTO users (id, name, email, password) VALUES (2, 'Bob', 'bob@example.com', 'password456')")

# commit the changes
conn.commit()

# close the connection
conn.close()
