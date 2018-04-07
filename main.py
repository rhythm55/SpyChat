from spy_details import Spy,friends, ChatMessage,chats
import csv
import menu
from termcolor import colored

print colored("Welcome to SpyChat", 'cyan', attrs=['bold'])

# default spy or new spy
user = raw_input(colored("you want to continue as default user or create your account : ", "yellow"))

if user == 'default':
    spy = Spy('Ms.rhythm', 21, 3, 4)
    # display function in spy_details displays information about spy
    spy.display_info('Ms.rhythm', 21, 3, 4)
else:
    # fetching details from new spy
    name = raw_input("Enter your spy name: ")
    if len(name) > 0:
        salutation = raw_input("what should we call you " + name + " (Mr. or Ms.)? ")
        name = salutation + "." + name
        print("Glad to have you here " + name)
        print("Alright " + name + " We would like to know a little bit more about you...")

        # checking weather age of spy is valid or not
        age = int(raw_input("what is your age? "))
        if age < 18 or age > 60:
            print("sorry! your age is not valid to be a spy")
            exit()
        else:
            experience = int(raw_input("for how many years you are working as a spy? "))
            rating = float(raw_input("what is your rating(out of 5)? "))

            # comments according to the rating of spy
            if rating >= 4.5:
                print("good ace!")
            elif rating < 4.5 and rating >= 3.5:
                print("you are one of good ones!")
            elif rating < 3.5 and rating >= 2.5:
                print("you can always do better!")
            else:
                print("we can always you somebody to help in the office")

            print("thanks for telling the information about you...")
            spy = Spy(name, age, experience, rating)
            # display function in spy_details displays information about spy
            spy.display_info(name, age, experience, rating)
    else:
        # if enter key is pressed it will be considered as invalid
        print("please enter a valid name")
        exit()


# ------- start chat -----
def start_chat():
    # load_friends() is a function which loads all the friends stored in friends.csv
    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], age=int(row[1]), experience=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # load_chats() is a function which loads all the chats of spies stored in chats.csv
    def load_chats():
        with open("chats.csv", 'rU') as chat:
            reader = csv.reader(chat)
            for row in reader:
                try:
                    chats.append(ChatMessage(sent_by_me=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue

    # both functions are called so that chats and list of friends are loaded before its usage
    load_friends()
    load_chats()

    # Menu of SpyChat
    show_menu = True
    while(show_menu):
        print("----- MENU -----")
        # menu_choices:
        print colored(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application", "yellow")
        menu_choice = int(input("enter your choice: "))
        if menu_choice == 1:
            # passed current spy to provide info of current spy
            menu.spy_status(spy)
        elif menu_choice == 2:
            # passed current spy to provide rating of spy
            e = menu.add_friend(spy)
            # e stores no of friends of spy
            print colored("your no of friends: " + str(e), "blue")
        elif menu_choice == 3:
            # passed current spy to provide rating of spy
            menu.send_a_message(spy)
        elif menu_choice == 4:
            # passed current spy to provide rating of spy
            menu.read_a_message(spy)
        elif menu_choice == 5:
            # no_chat stores value returned by read_chat if there exist a chat no_chat will be 1
            no_chat = menu.read_chat(spy)
            if no_chat != 1:
                print colored("no messages exchanged yet", "red")
        if menu_choice == 6:
            # when show_menu value become false it will exit from while loop
            show_menu = False


# calling the start_chat() function that includes menu and loads friends from friends.csv and chats from chat.csv
start_chat()

