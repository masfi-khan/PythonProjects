import turtle
import math

#individual user account; user profile
class User:
    def _init_(self, username):
        self.name = username
        self.connections = []
        self.id = number(numb_users)
        self.network = None

    def set_Network(network):
        self.network = network

    def id(self, id):
        self.id = number

    def connections(self, friend):
        self.connections.append(friend)

    def makeAccount(self):
        create_account = input("Do you want to create an user account? Reply 'yes' or 'no'.")
        if create_account == "yes":
            choose_username = input("What username do you want?")
            print("You are" + " " + choose_username)
        else:
            print("Alright then.")

    def get_username(self):
        return self.name

    def get_id(self):
        return self.id

    def get_connections(self):
        return self.connections

#all accounts in the social network
class Network:

    def _init_(self, User1, User2):
        self.accounts = []

    def numb_users(self):
        n = len(self.accounts)

        for i in range(n):
            i += 0
            self.id = self.accounts[i]
            self.accounts.append(self.id)

        print(self.accounts)

#add new user
    def add_user(self, User1, User2):
        taken = True
        while taken:
            if username in self.accounts:
                print("This username is already taken. Choose another one.")
            else:
                self.accounts.append(user)
                user.set_Network(self)
                user.set_id(numb_users)
                taken = False

    # def set_self.id = number(numb_users)

#check user's existence, add friends
    def addConnectionNet(self, User1, User2):
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
                print(User1.connections)
                print(User2.connections)

def main():
#Define the program flow for your user interface here.
#set user properties to new user, add network properties, add them to account list + id number
    new_user = User()
    new_user.makeAccount()
    User1 = User()

    new_user = User()
    new_user.makeAccount()
    User2 = User()

    user_network = Network()
    # new_user.add_userUser1, User2)
    add_friend = input("Do you want to add the user to your connections?")
    if add_friend == "yes":
        user_network.user1.addConnectionNet.append(User1)





# #Runs your program.
if __name__ == '__main__':
    main()
