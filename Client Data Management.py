import sqlite3
from customer import customer_verification
from database import customer_table
def client_insertion():

    a = customer_table()
    c = a.customer_verification()
    c.execute("""INSERT INTO customer(name, email, password) VALUES (?, ?, ?)""",
                   (name,email,password))]]
    print("Account created successfully")