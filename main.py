print("Welcome to SpyChat")
import spy_details
import menu

# default user or new user
user = input("you want to continue as default user or create your account : ")
user = spy_details.spy(user)


# Menu of SpyChat
show_menu = True
while(show_menu):
    print("----- MENU -----")
    # menu_choices:
    print(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application ")
    menu_choice = int(input("enter your choice: "))
    if menu_choice == 1:
        menu.spy_status()
    elif menu_choice == 2:
        e = menu.add_friend(user)
        print("your no of friends:" + str(e))
    if menu_choice == 6:
        show_menu = False





