print("Welcome to SpyChat")
from spy_details import spy
import menu

# default user or new user
user = input("you want to continue as default user or create your account : ")
user = spy(user)
# user contains the current spy name and rating

# Menu of SpyChat
show_menu = True
while(show_menu):
    print("----- MENU -----")
    # menu_choices:
    print(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application ")
    menu_choice = int(input("enter your choice: "))
    if menu_choice == 1:
        # passed user to provide info of current spy
        menu.spy_status(user)
    elif menu_choice == 2:
        # passed user to provide rating of spy
        e = menu.add_friend(user)
        # e stores no of friends of spy
        print("your no of friends: " + str(e))
    if menu_choice == 6:
        show_menu = False





