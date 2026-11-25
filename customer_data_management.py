import sqlite3 as sql
from Update_plan import update_plan
from Subscription_Management import show_plans
def customer_insert(name, email, password):
    conn = sql.connect("customer.db")
    c = conn.cursor()
    c.execute("INSERT INTO customer(name,email,password) VALUES(?,?,?)",(name, email, password))
    print("customer inserted successfully\n")
    conn.commit()
    conn.close()

def customer_find(name, email, password):
    conn = sql.connect("customer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customer WHERE name = ? AND email = ? AND password = ?",(name, email,password))
    k=c.fetchall()

    if not k:
        print("customer not found")
        return
    else:
        print("customer found successfully")
        print(k)
        print(f'Your details: \n Name:{name} \n Email:{email} \n')

    id_ = k[0][0]
    while True:
        print("1.Show Plans")
        print("2.Login To Another Account")
        print("3.Update Plan")
        print("4.Go back")
        choose = int(input("Choose your option: "))
        if choose == 1:
            show_plans(id_,name,email)
        elif choose == 2:
            name = input("Enter your name: ").capitalize()
            email = input("Enter your email: ").strip().lower()
            password = input("Enter your password: ")
            customer_find(name, email, password)
        elif choose == 3:
            update_plan(id_,name,email)
        elif choose == 4:
            print("Logout Successfully\n")
            break
        else:
            print("Invalid option")