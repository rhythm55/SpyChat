from spy_details import Spy,friends, ChatMessage,chats,Friend
import csv
import menu
from termcolor import colored

# welcome message for spy
print colored("Welcome to SpyChat", 'cyan', attrs=['bold'])

# list to store the spies
spies = []

# Load_spy loads the spy details stored in spy.csv
def load_spy():
    with open('spy.csv', 'rU') as spy_data:
        reader = csv.reader(spy_data)
        for row in reader:
            try:
                spy = Spy(name=row[0], password=row[1], age=int(row[2]), experience=int(row[3]), rating=float(row[4]))
                spies.append(spy)
            except IndexError:
                pass
            continue
load_spy()

# auth is authentication it will be true until user is not authenticated successfully
auth = True
while auth is True:
    user = raw_input(colored("enter your choice- \n 1.Login \n 2.Create new account \n 3.Default User \n", "yellow"))
    # for login
    if int(user) == 1:
        username = raw_input("enter your username :")
        password = raw_input("enter your password:")
        login = False
        for i in range(len(spies)):
            if username == spies[i].name and password == spies[i].password:
                spy = Spy(spies[i].name, spies[i].password, spies[i].age, spies[i].experience, spies[i].rating)
                print colored("successfully logged in", "green")
                Spy.display(spy)
                login = True
                auth = False
        if login is False:
            print colored("wrong user name or password", "red")
            auth = True
    # for creating new spy account
    elif int(user) == 2:
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
                print colored("sorry! your age is not valid to be a spy", "red")
                auth = True
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

                password = raw_input("set your password: ")

                print("thanks for telling the information about you...")
                for i in range(len(spies)):
                    print("for")
                    # checking if the account already exist with same information
                    if name == spies[i].name:
                        print colored("account already exists", "red")
                        auth = True
                    else:
                        print colored("account created", "green")
                        print colored("user name: " + name + "\npassword:" + password, "green")
                        # adding spy
                        spy = Spy(name, password, age, experience, rating)
                        spies.append(spy)
                        Spy.display(spy)
                        with open('spy.csv','a') as spy_data:
                            writer = csv.writer(spy_data)
                            writer.writerow([name, password, age, experience, rating])
                            auth = False
                        break
        else:
            # if enter key is pressed it will be considered as invalid
            print("please enter a valid name")
            auth = True

    # for default user
    elif int(user) == 3:
        spy = Spy('Ms.Rhythm', 'default', 21, 3, 4)
        Spy.display(spy)
        auth = False
    else:
        print("incorrect input")
        auth = True


# ------- start chat -----
def start_chat():
    # load_friends is a function which loads all the friends stored in friends.csv
    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friend = Friend(friend_of=row[0], name=row[1], experience=int(row[2]), rating=float(row[3]))
                    friends.append(friend)
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
    # menu will be displayed till show_menu becomes false
    show_menu = True
    while(show_menu):
        print("----- MENU -----")
        # menu_choices:
        print colored(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application", "yellow")
        menu_choice = int(input("enter your choice: "))
        if menu_choice == 1:
            # display current status, updates status with new status and displays all previous statuses for selection of current status
            # add_status function for adding/updating status
            # passed current spy to provide info of current spy
            menu.spy_status(spy)
        elif menu_choice == 2:
            # check the eligibility of friend and if it is friend is added to the friend list of current spy
            # passed current spy to provide rating of spy
            menu.add_friend(spy)
        elif menu_choice == 3:
            # it calls select friend which display list of friends of current spy and returns the index of selected friend
            # encrypts the text in a image using steganography encode
            # modifies chats.csv to keep record of chat
            # passed current spy to provide rating of spy
            menu.send_a_message(spy)
        elif menu_choice == 4:
            # it calls select friend which display list of friends of current spy and returns the index of selected friend
            # decrypts the text in a image using steganography decode
            # modifies chats.csv to keep record of chat
            # passed current spy to provide rating of spy
            menu.read_a_message(spy)
        elif menu_choice == 5:
            # display chat of current spy with his/her friend using chats.csv
            # no_chat stores value returned by read_chat if there exist a chat no_chat will be 1
            no_chat = menu.read_chat(spy)
            if no_chat != 1:
                print colored("no messages exchanged yet", "red")
        if menu_choice == 6:
            # when show_menu value become false it will exit from while loop
            show_menu = False


# calling the start_chat() function that includes menu and loads friends from friends.csv and chats from chat.csv
start_chat()

