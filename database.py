import sqlite3

conn = sqlite3.connect("customer.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS customer(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT,
           email TEXT UNIQUE,
           password TEXT
           )''')




# Monthly

conn = sqlite3.connect("customer.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS MonthlyCustomer(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
        )''')


# Quarterly

cursor.execute('''CREATE TABLE IF NOT EXISTS QuarterlyCustomer(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
        )''')


# Yearly


cursor.execute('''CREATE TABLE IF NOT EXISTS YearCustomer(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
        )''')

conn.commit()
conn.close()
