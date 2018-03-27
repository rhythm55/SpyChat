status_messages=['i am a spy','james bond']

def spy_status():
    current_status_message = None
    show_menu=True
    while(show_menu):
        # menu_choices
        print("What do you want to do? \n1.Add a status update \n2.close application")
        menu_choice=int(input("enter your choice: "))
        if menu_choice==1:
            print("you choose to add a status")
            current_status_message=add_status(current_status_message)
            print("your status is : "+current_status_message)
        else:
            show_menu=False

def add_status(current_status_message):

    if current_status_message!=None:
        print("your current status message is: "+current_status_message)
        default = input("Do you want to select from the older status (Y/N)? ")
        if default.upper() == 'N':
            new_status_message = input("what status message you want to set? \n")
            if len(new_status_message) > 0:
                status_messages.append(new_status_message)
                current_status_message=new_status_message
            else:
                print("invalid status message")
                spy_status()
        else:
            print("select which old status you want as your current status? ")
            item_position = 1
            for message in status_messages:
                print(str(item_position)+"."+message)
                item_position = item_position+1
            message_selection = int(input("\n choose from above messages:"))
            if message_selection > 0:
                current_status_message=status_messages[message_selection-1]
    else:
        print("you don't have any status message currently! ")
        new_status_message=input("enter a status message : \n")
        if len(new_status_message) > 0:
            current_status_message = new_status_message
            status_messages.append(current_status_message)
        else:
            print("invalid status message")
            spy_status()

    return current_status_message

