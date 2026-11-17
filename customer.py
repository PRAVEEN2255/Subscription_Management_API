import re
from database import customer_table
def customer_verification():
    print("1.Create Customer Account")
    print("2.Login To Exited Account")
    choose = int(input("Choose your option: "))
    if choose == 1:
        name = input("Enter your name: ").upper()
        email = input("Enter your email: ").strip().lower()
        if "@" not  in  email and "." not in email:
            print("Please enter a valid email address")
            return None
        password = input("Enter your password: ")
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(pattern, password):
            print("Password is valid")
        else:
            print("Password is not valid")
    return customer_verification()

