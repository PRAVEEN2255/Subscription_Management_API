import re
from customer_data_management import *
def customer_verification():
    while True:
     print("1.Create Customer Account")
     print("2.Login To Exiting Account")
     print("3.GO Back\n")
     choose = int(input("Choose your option: "))
     if choose == 1:
        while True:
            name = input("Enter your name: ").capitalize()
            if not name.isalpha():
              print("Not a valid name")
            else:
              break
        while True:
            email = input("Enter your email: ").strip().lower()
            if ".com" in email and "@" in email:
                break
            else:
                print("Please enter a valid email address")
        while True:
            password = input("Enter your password: ")
            pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
            if re.match(pattern, password):
                print("Password is valid")
                customer_insert(name, email, password)
                while True:
                    print("1.Show Plans")
                    print("2.Login To Another Account")
                    print("3.GO Back\n")
                    choose = int(input("Choose your option: "))
                    if choose == 1:
                        customer_find(name, email, password)
                        break
                    elif choose == 2:
                        name = input("Enter your name: ").capitalize()
                        email = input("Enter your email: ").strip().lower()
                        password = input("Enter your password: ")
                        customer_find(name, email, password)
                    elif choose == 3:
                        print("Logout Successfully")
                        break
                    else:
                        print("Invalid option")
                break
            else:
             print("Password is not valid")

     elif choose == 2:
        name = input("Enter your name: ").capitalize()
        email = input("Enter your email: ").strip().lower()
        password = input("Enter your password: ")
        customer_find(name, email, password)


     elif choose == 3:
         print("Logout Successfully")
         break
     else:
         print("Invalid option")
