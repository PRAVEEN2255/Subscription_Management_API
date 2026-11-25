from customer_service_management import *
import sqlite3 as sql
def update_plan(id_,name,email):
    while True:
        print("1.Month Plan")
        print("2.Quarter Plan")
        print("3.Year Plan")
        print("4.GO Back")
        choose = int(input("Choose your option: "))
        if choose == 1:
            conn = sql.connect("customer.db")
            cursor = conn.cursor()  # Check Monthly
            cursor.execute("SELECT * FROM MonthlyCustomer  WHERE name = ? AND email = ?",(name,email))
            customer = cursor.fetchone()
            if customer is None:
                cursor.execute("DELETE FROM QuarterlyCustomer WHERE name = ? and email = ?", (name,email))
                cursor.execute("DELETE FROM YearCustomer WHERE name = ? and email = ?", (name,email))
                conn.commit()
                conn.close()
                print("Plan removed Successfully")
                print("========== MONTH PLAN ==========")
                duration = 30
                price = 200
                print(f'Duration: {duration} days \nPrice: INR {price}\n')
                choose = input("TYPE 'PAY' TO MAKE THE PAYMENT: ")
                if choose == "PAY":
                    print("Payment Successfully Done")
                    monthly_customers(id_, name, email)
                else:
                    print("Invalid Payment")
            elif name == customer[1] and email == customer[2]:
                print("Customer already exists Plan.")


        elif choose == 2:
            conn = sql.connect("customer.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM QuarterlyCustomer WHERE name = ? AND email = ?",
                (name,email))
            quarter = cursor.fetchone()
            if quarter is None:
                cursor.execute("DELETE FROM MonthlyCustomer WHERE name = ? and email = ?", (name,email))
                cursor.execute("DELETE FROM YearCustomer WHERE name = ? and email = ?", (name,email))
                conn.commit()
                conn.close()
                print("Plan removed Successfully")
                print("========== QUARTER PLAN ==========")
                duration = 120
                price = 500
                print(f'Duration: {duration} days \nPrice: INR {price}\n')
                choose = input("TYPE 'PAY' TO MAKE THE PAYMENT: ")
                if choose == "PAY":
                    print("Payment Successfully Done")
                    quarterly_customers(id_, name, email)
                else:
                    print("Invalid Payment")
            elif name == quarter[1] and email == quarter[2]:
                print("Customer already exists Plan.")


        elif choose == 3:
            conn = sql.connect("customer.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM YearCustomer  WHERE name = ? AND email = ?",
                       (name,email))
            year = cursor.fetchone()
            print(year)
            if year is None:
                cursor.execute("DELETE FROM MonthlyCustomer WHERE name = ? and email = ?", (name,email))
                cursor.execute("DELETE FROM QuarterlyCustomer WHERE name = ? and email = ?",(name,email))
                conn.commit()
                conn.close()
                print("Plan removed Successfully")
                print("========== YEAR PLAN ==========")
                duration = 365
                price = 1000
                print(f'Duration: {duration} days \nPrice: INR {price}\n')
                choose = input("TYPE 'PAY' TO MAKE THE PAYMENT: ")
                if choose == "PAY":
                       print("Payment Successfully Done")
                       yearly_customers(id_, name, email)
                else:
                    print("Invalid Payment")
            elif name == year[1] and email == year[2]:
                print("Customer already exists Plan.")
        elif choose == 4:
            print("Log out Successfully\n")
            break
        else:
            print("Invalid option")


