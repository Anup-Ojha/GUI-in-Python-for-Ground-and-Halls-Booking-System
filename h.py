import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect("user_database.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
cursor.execute('''INSERT INTO users VALUES (1,'anup','ojha'); ''')
# Commit changes and close the connection
conn.commit()
conn.close()
