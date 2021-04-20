from entities.user import User
from repositories.userdata import UserData

def main():
    user_data = UserData("src/data/data.db")

    print("Creating user")

    username = input("Username: ")
    password = input("Password: ")
    user = User(username,password)

    user_data.create(user)

    print("User is in register now")
    print("Here's how register looks like")
    for i in user_data.readall():
        print(i)

    user_data.deleteall()

main()