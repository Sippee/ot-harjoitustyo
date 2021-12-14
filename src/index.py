from services.service import Service, UserError

service_handler = Service()

option = "0"
    
while option != "4":
    if option=="2":
        option=str(input("What do you want to do? \n3: Logout \n4: Exit the application \nSelect your option. \n"))
    else:
        option=str(input("What do you want to do? \n1: Create a new user \n2: Login \n3: Logout \n4: Exit the application \nSelect your option \n"))

    if option=="1":
        name=input("Name:")
        password=input("Password:")

        try:
            service_handler.create_user(name, password)
            print("\nYou created a user\n")
        except UserError:
            continue

    if option=="2":
        name=input("Name:")
        password=input("Password:")

        try:
            service_handler.login(name,password)
            print("\nYou logged in\n")
        except UserError:
            continue

    if option=="3":
        service_handler.logout()
        print("\nYou logged out\n")

#väliaikainen
