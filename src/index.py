from services.service import Service

def create_user(name, password):
    Service.create_user(name,password)

def login(name, password):
    Service.login(name,password)

def logout():
    Service.logout()

if __name__=="__main__":
    option = "0"
    
    while option is not "4":
        option=str(input("Mitä haluat tehdä? 1: Luo tunnus, 2: Kirjaudu sisään, 3: Kirjaudu ulos, 4: Lopeta sovellus"))
        if option=="1":
            name=input("Anna nimi:")
            password=input("Anna salasana:")
            #create_user(name,password)
            print("Loit tunnuksen")

        if option=="2":
            name=input("Anna nimi:")
            password=input("Anna salasana:")
            #login(name,password)
            print("Olet kirjautunut sisään")

        if option=="3":
            #logout()
            print("Olet kirjautunut ulos")

#väliaikainen