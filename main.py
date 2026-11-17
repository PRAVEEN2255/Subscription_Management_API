from customer import customer_verification
while True:
    print("==================================")
    print("Welcome to subscription management")
    print("==================================\n")
    print("1. Customer")
    print("2. subscription due renewal")
    print("3. Exit")

    choose = int(input("Choose your option: "))
    if choose == 1:
        customer_verification()
    elif choose == 2:
     print("Thank you for your time")
    elif choose == 3:
     print("Thank you for your time")
     break
    else:
     print("Invalid option")
