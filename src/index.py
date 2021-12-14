from services.service import Service, UserError

service_handler = Service()

option = "0"
    
while option != "4":
    if option=="2":
        option=str(input("Mitä haluat tehdä? \n3: Kirjaudu ulos, \n4: Lopeta sovellus \nMitä tehdään? \n"))
    else:
        option=str(input("Mitä haluat tehdä? \n1: Luo tunnus, \n2: Kirjaudu sisään, \n3: Kirjaudu ulos, \n4: Lopeta sovellus \nMitä tehdään? \n"))

    if option=="1":
        name=input("Anna nimi:")
        password=input("Anna salasana:")

        try:
            service_handler.create_user(name, password)
            print("Loit tunnuksen")
        except UserError:
            continue

    if option=="2":
        name=input("Anna nimi:")
        password=input("Anna salasana:")

        try:
            service_handler.login(name,password)
            print("Olet kirjautunut sisään")
        except UserError:
            continue

    if option=="3":
        service_handler.logout()
        print("Olet kirjautunut ulos")

#väliaikainen
