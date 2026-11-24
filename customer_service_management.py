import sqlite3 as sql

def monthly_custs(id_,name, email):
    conn = sql.connect("customer.db")
    c = conn.cursor()
    c.execute("INSERT INTO MonthlyCustomer(id,name,email) VALUES(?,?,?)",(id_,name, email))
    print("Monthly customer inserted successfully\n")
    conn.commit()
    conn.close()


def quarterly_custs(id_,name, email):
    conn = sql.connect("customer.db")
    c = conn.cursor()
    c.execute("INSERT INTO QuarterlyCustomer(id,name,email) VALUES(?,?,?)",(id_,name, email))
    print("Quarterly customer inserted successfully\n")
    conn.commit()
    conn.close()



def yearly_custs(id_,name, email):
    conn = sql.connect("customer.db")
    c = conn.cursor()
    c.execute("INSERT INTO YearCustomer(id,name,email) VALUES(?,?,?)",(id_,name, email))
    print("Yearly customer inserted successfully\n")
    conn.commit()