import turtle
import math

#individual user account; user profile
class User:
    def __init__(self, username):
        self.name = username
        self.connections = []

    #     self.id = number(numb_users)
    #     self.network = None
    #
    # def set_Network(network):
    #     self.network = network
    #
    # def id(self, id):
    #     self.id = number

    def connections(self, friend):
        self.connections.append(friend)

    def makeAccount(self):
            choose_username = input("What username do you want?")
            print("You are" + " " + choose_username)

    def get_username(self):
        return self.name
    #
    # def get_id(self):
    #     return self.id

    def get_connections(self):
        return self.connections

#all accounts in the social network
class Network:

    def __init__(self):
        self.accounts = ["Masfi", "Yuki"]

    def numbusers(self):
        n = len(self.accounts)
        print(self.accounts)

    #     for i in range(n):
    #         i += 0
    #         self.id = self.accounts[i]
    #         self.accounts.append(self.id)
    #
    # def get_numbusers(self):
    #     return self.accounts

#add new user
    def add_user(self, User1):
        # taken = True
        # while taken:
        #     username = User1.set_name(self)
        #     if username in self.accounts:
        #         print("This username is already taken. Choose another one.")
        #     else:
        self.accounts.append(User1)
        # User1.set_Network(self)
        # User1.set_id(numb_users)
                # taken = False

#check user's existence, add friends
    def addConnectionNet(self, User1, User2):
        n = len(self.accounts)
        for i in range(n):
            if User1 in self.accounts:
                return True
            else:
                print("This user does not exist.")
                return False

            if User2 in self.accounts:
                return True
            else:
                print("This user does not exist.")
                return False

            if User1 in User2.connections:
                print("You are already connected to this user.")
            else:
                User1.connections.append(User2)
                User2.connections.append(User1)

    def get_addConnectionNet(self):
        return User1.connections
        return User2.connections

def main():
#Define the program flow for your user interface here.
    user_network = Network()
    new_user = User("mk")
    user_input = input("Do you want to create an account, add a friend, or view your profile?")
    if user_input == "create an account":
        new_user.makeAccount()
        User1 = User("wf")
        user_network.add_user(User1)
        print(get_numbusers)
    # if user_input == "add a friend":
        # new_user = User()
        # User1 = User()
        # User2 = User()
        # user_network = Network()
        # x = input("Which user do you want to connect with?")
        # user_network.addConnectionNet(User1, User2)

        # user_network.add_user(User1)

        # User1 = Network()


#check for friend's existence, add friend to connection if not already added





# #Runs your program.
if __name__ == '__main__':
    main()
