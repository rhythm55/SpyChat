print("Welcome to SpyChat")
import spy_details

# default user or new user
user = input("you want to continue as default user or create your account : ")
if user == "default":
    # details of default spy stored in spy_details.py
    spy_details.detail(spy_details.spy_name, spy_details.spy_salutation, spy_details.spy_age, spy_details.spy_experience, spy_details.spy_rating)
else:
    # fetching details from new_spy function in spy_details.py
    spy_details.new_spy()

# Menu of SpyChat
option = 1
while(option < 6 and option > 0):
    print("----- MENU -----")
    print(" 1.Add a status update \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Read chat from a user \n 6.Close application ")
    option = int(input("enter option number of menu : "))






