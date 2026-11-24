from Payament_Management import *
def show_plans(id_,name,email):
    while True:
        print("1.Month Plan")
        print("2.Quarter Plan")
        print("3.Year Plan")
        print("4.GO Back")
        choose = int(input("Choose your option: "))
        if choose == 1:
            print("========== MONTH PLAN ==========")
            duration = 30
            price = 200
            print(f'Duration: {duration} days \nPrice: INR {price}\n')
            print("1.GO TO Payment Page")
            print("2.Go Back")
            choose = int(input("Choose your option: "))
            if choose == 1:
                payment_mode(id_,name,email,duration)
            elif choose == 2:
                print("Log out Successfully")
            else:
                print("Invalid option")

        elif choose == 2:
            print("========== QUARTER PLAN ==========")
            duration = 120
            price = 500
            print(f'Duration: {duration} days \nPrice: INR {price}\n')
            print("1.GO TO Payment Page")
            print("2.Go Back")
            choose = int(input("Choose your option: "))
            if choose == 1:
                payment_mode(id_,name,email,duration)
            elif choose == 2:
                print("Log out Successfully")
            else:
                print("Invalid option")

        elif choose == 3:
            print("========== YEAR PLAN ==========")
            duration = 365
            price = 1000
            print(f'Duration: {duration} days \nPrice: INR {price}\n')
            print("1.GO TO Payment Page")
            print("2.Go Back")
            choose = int(input("Choose your option: "))
            if choose == 1:
                payment_mode(id_,name,email,duration)
            elif choose == 2:
                print("Log out Successfully")
            else:
                print("Invalid option")

        elif choose == 4:
            print("Log out Successfully")

            break
        else:
            print("Invalid option")


