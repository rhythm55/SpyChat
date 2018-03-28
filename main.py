print("Welcome to SpyChat")
import spy_details
import menu
# default user or new user
user = input("you want to continue as default user or create your account : ")
if user == "default":
    # details of default spy stored in spy_details.py
    spy_active = spy_details.default_spy()
else:
    # fetching details from new_spy function in spy_details.py
    spy_details.new_spy()

# Menu of SpyChat
show_menu = True
while(show_menu):
    print("----- MENU -----")
    # menu_choices
    print(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application ")
    menu_choice = int(input("enter your choice: "))
    if menu_choice == 1:
        menu.spy_status()
    elif menu_choice == 2:
        e = menu.add_friend()
        print("your no of friends:" + str(e))
    if menu_choice == 6:
        show_menu = False





