status_messages = []

# function add and update status of spy
def spy_status():
    current_status_message = None
    show_menu=True
    while(show_menu):
        # menu_choices
        print("What do you want to do? \n1.Add \ update status \n2.close application")
        menu_choice = int(input("enter your choice: "))
        if menu_choice == 1:
            print("you choose to add a status")
            current_status_message=add_status(current_status_message)
            print("your status is : "+current_status_message)
        else:
            show_menu = False

def add_status(current_status_message):

    # user already have a status
    if current_status_message != None:
        print("your current status message is: "+current_status_message)
        default = input("Do you want to select from the older status (Y/N)? ")
        # user want to add new status
        if default.upper() == 'N':
            new_status_message = input("what status message you want to set? \n")
            if len(new_status_message) > 0:
                status_messages.append(new_status_message)
                current_status_message=new_status_message
            else:
                print("invalid status message")
                spy_status()
        # user wants to select status from list of old statuses
        else:
            print("select which old status you want as your current status? ")
            item_position = 1
            for message in status_messages:
                print(str(item_position)+"."+message)
                item_position = item_position+1
            message_selection = int(input("\n choose from above messages:"))
            if message_selection > 0:
                current_status_message=status_messages[message_selection-1]

    # user do not have any status yet
    else:
        print("you don't have any status message currently! ")
        new_status_message=input("enter a status message : \n")
        if len(new_status_message) > 0:
            current_status_message = new_status_message
            status_messages.append(current_status_message)
        else:
            print("invalid status message")
            spy_status()

    # function will return current message updated from cases accordingly
    return current_status_message

friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
import spy_details

def add_friend():
    f_name = input("enter your friend's name: ")
    f_salu = input(f_name+"'s salutation? ")
    f_name = f_salu + "." + f_name
    f_age = int(input("age? "))
    f_rating = int(input("spy rating?"))
    f_is_online = input("online status? ")

    if len(f_name) > 0 and f_age > 12:
        friends_name.append(f_name)
        friends_age.append(f_age)
        friends_rating.append(f_rating)
        friends_is_online.append(f_is_online)
        print(f_name+" added successfully as your friend")
    else:
        print("sorry! invalid entry. We can't add spy with details you provided")
    return len(friends_name)

