from user import User
import pickle

class UserData:
    def __init__(self):
        pass

    def create(self, user):
        data = []
        with open("data.txt", "rb") as f:
            while True:
                try:
                    data.append(pickle.load(f))
                except EOFError:
                    break
        #list1=[user,user1,user2]
        with open("data.txt", "wb") as d:
            pickle.dump(data, d)


    def readall(self):
        with open("data.txt", "rb") as d:
            data = pickle.load(d)
        for i in data:
            print(i)

#Testausta varten
def main():
    ab = UserData()
    user1 = User("Markus", "keijo")
    user2 = User("Keijo", "keijotin")
    user3 = User("ab", "ree")
    #ab.create(user1,user2,user3)
    #ab.create(user2)
    ab.create(user3)
    ab.readall()

main()