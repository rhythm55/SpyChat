from spy_details import Spy
import menu

print("Welcome to SpyChat")

# default user or new user
user = raw_input("you want to continue as default user or create your account : ")

if user=='default':
    spy = Spy('rhythm', 'Ms', 21, 3, 4)
else:
    # fetching details from new spy
    name = raw_input("Enter your spy name: ")
    if len(name) > 0:
        salutation = raw_input("what should we call you " + name + " (Mr. or Ms.)? ")
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
            spy = Spy(name, salutation, age, experience, rating)
# user contains the current spy name and rating
    else:
        print("please enter a valid name")
        exit()



# Menu of SpyChat
show_menu = True
while(show_menu):
    print("----- MENU -----")
    # menu_choices:
    print(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application ")
    menu_choice = int(input("enter your choice: "))
    if menu_choice == 1:
        # passed user to provide info of current spy
        menu.spy_status(spy)
    elif menu_choice == 2:
        # passed user to provide rating of spy
        e = menu.add_friend(spy)
        # e stores no of friends of spy
        print("your no of friends: " + str(e))
    elif menu_choice == 3:
        menu.send_a_message()
    elif menu_choice == 4:
        menu.read_a_message()
    if menu_choice == 6:
        show_menu = False





