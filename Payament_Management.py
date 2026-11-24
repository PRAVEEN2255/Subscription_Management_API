from customer_service_management import *
import _sqlite3 as sql
def payment_mode(id_,name,email,duration):

    choose = input("TYPE 'PAY' TO MAKE THE PAYMENT ")
    if choose == 'PAY':
        if duration == 30:
            conn = sql.connect("customer.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM MonthlyCustomer WHERE id = ?",
                (id_,)
            )
            customer = cursor.fetchone()
            if  id_== customer[0]:
                print("Customer already exists in the table.")
            else:
                monthly_custs(id_, name, email)
                print("Made payment successfully")
                print("THANK YOU FOR PURCHASING THE MONTHLY PLAN")
        elif duration == 120:
            conn = sql.connect("customer.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM QuarterlyCustomer WHERE id = ?",
                (id_,)
            )
            customer = cursor.fetchone()
            print(customer)
            if id_== customer[0]:
                print("Customer already exists in the table.")
            else:
                quarterly_custs(id_, name, email)
                print("Made payment successfully")
                print("THANK YOU FOR PURCHASING THE QUARTERLY PLAN")
        elif duration == 365:
            conn = sql.connect("customer.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM YearCustomer WHERE id = ?",
                (id_,)
            )
            customer = cursor.fetchone()
            if id_== customer[0][0]:
                print("Customer already exists in the table.")
            else:
                yearly_custs(id_, name, email)
                print("Made payment successfully")
                print("THANK YOU FOR PURCHASING THE YEARLY PLAN")
        else:
            print("Invalid option")
    else:
        print("Invalid option")