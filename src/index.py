from services.service import Service, UserError

service_handler = Service()

from tkinter import Tk
from ui.ui import UI

def main():

    window = Tk()
    window.title('Coin Collector Game')

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == '__main__':
        main()

"""option = "10"
logged_in = False
    
while option != "4":
    if logged_in:
        option=str(input("What do you want to do?\n0: Play Coin Collector  \n3: Logout \n4: Exit the application \n5: Top 10 \nSelect your option. \n"))
    else:
        option=str(input("What do you want to do? \n1: Create a new user \n2: Login \n4: Exit the application \n5: Top 10 \nSelect your option \n"))

    if option=="1" and not logged_in:
        name=input("Name:")
        password=input("Password:")

        try:
            service_handler.create_user(name, password)
            print("\nYou created a user\n")
            logged_in=True
        except UserError:
            continue

    if option=="2" and not logged_in:
        name=input("Name:")
        password=input("Password:")

        try:
            service_handler.login(name,password)
            print("\nYou logged in\n")
            logged_in=True
        except UserError:
            continue

    if option=="3" and logged_in:
        service_handler.logout()
        logged_in=False
        print("\nYou logged out\n")

    if option=="4":
        logged_in=False
        break

    if option=="0" and logged_in:
        print(f"You collected {service_handler.game()} points")


    if option =="5":
        for row in service_handler.top10_hiscore():
            print(f"{row}\n")
"""
# OPTION 4 NOT WORKING ATM FOR SOME REASON
