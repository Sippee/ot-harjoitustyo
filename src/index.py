from services.service import Service, UserError

service_handler = Service()

option = "10"
logged_in = False
    
while option != "4":
    if logged_in:
        option=str(input("What do you want to do?\n0: Play Coin Collector  \n3: Logout \n4: Exit the application \nSelect your option. \n"))
    else:
        option=str(input("What do you want to do? \n1: Create a new user \n2: Login \n4: Exit the application \nSelect your option \n"))

    if option=="1":
        name=input("Name:")
        password=input("Password:")

        try:
            service_handler.create_user(name, password)
            print("\nYou created a user\n")
            logged_in=True
        except UserError:
            continue

    if option=="2":
        name=input("Name:")
        password=input("Password:")

        try:
            service_handler.login(name,password)
            print("\nYou logged in\n")
            logged_in=True
        except UserError:
            continue

    if option=="3":
        service_handler.logout()
        logged_in=False
        print("\nYou logged out\n")

    if option=="4":
        logged_in=False
        break

    if option=="0":
        print(f"You collected {service_handler.game()} points")

#väliaikainen
