import sqlite3
from customer import customer_verification
def customer_table():
    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXITED customer(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL AND UNIQUE(email),
    password TEXT NOT NULL)
    """)
    conn.commit()
    print("Account created successfully")
    conn.close()

