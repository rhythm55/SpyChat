from datetime import datetime
from spy_details import ChatMessage,Spy,friends,ChatMessage

# data structure to hold list of spy's statuses
status_messages = []

# function add and update status of spy
def spy_status(spy):
    current_status_message = None
    show_menu=True
    while(show_menu):
        # menu_choices
        print("What do you want to do? \n1.Add \ update status \n2.close application")
        menu_choice = int(raw_input("enter your choice: "))
        if menu_choice == 1:
            print("you choose to add a status")
            spy.current_status_message = add_status(spy.current_status_message)
            print(spy.name + " status is : " + spy.current_status_message)
        else:
            show_menu = False

def add_status(current_status_message):

    # user already have a status
    if current_status_message != None:
        print("your current status message is: " + current_status_message)
        default = raw_input("Do you want to select from the older status (Y/N)? ")
        # user want to add new status
        if default.upper() == 'N':
            new_status_message = raw_input("what status message you want to set? \n")
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
            message_selection = int(raw_input("\n choose from above messages:"))
            if message_selection > 0:
                current_status_message=status_messages[message_selection-1]

    # user do not have any status yet
    else:
        print("you don't have any status message currently! ")
        new_status_message = raw_input("enter a status message : \n")
        if len(new_status_message) > 0:
            current_status_message = new_status_message
            status_messages.append(current_status_message)
        else:
            print("invalid status message")
            spy_status()

    # function will return current message updated from cases accordingly
    return current_status_message


def add_friend(spy):

    # details of friend
    name = raw_input("enter your friend's name: ")
    salutation = raw_input(name + "'s salutation? ")
    age = int(raw_input("age? "))
    experience = int(raw_input("experience ?"))
    rating = float(raw_input("spy rating?"))

    if len(name) > 0 and age > 12 and age > spy.rating:
        new_friend = Spy(name, salutation, age, experience, rating)
        friends.append(new_friend)
        print(name+" added successfully as your friend")
    else:
        print("sorry! invalid entry. We can't add spy with details you provided")

    # return no of friend spy have
    return len(friends)

# it will select a friend out of list of friends
def select_a_friend():
    i = 0
    # displaying list of friends of user
    print("list of your friends:")
    for friend in friends:  # fetching friends from friends list created in spy_details
        item_number = 0
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name, friend.age, friend.rating)
    index = int(raw_input("enter serial.no of friend you want to select "))
    # index will store index no of selected friend in friends list
    return index - 1

# ------------------- steganography -------------------------

from steganography.steganography import Steganography

def send_a_message():
    print("which friend you want to communicate with?")
    selected_friend = select_a_friend()
    # selected_friend contains index of friend selected via select_a_friend function
    original_image = raw_input("enter name of image you want to encode secret message with: ")
    output_path = 'output.jpg'
    text = raw_input("enter secret message you want to hide: ")
    Steganography.encode(original_image, output_path, text)
    # encode method of Steganography library will hide secrete message in selected image

    new_chat = ChatMessage(text, True)  # calling Chat class
    friends[selected_friend].chats.append(new_chat)  # appending in chats in friends list
    print("your secret message is ready")

def read_a_message():
    sender = select_a_friend()
    # sender stores index of friend whose message user want to read
    output_path = raw_input("enter the name of the image you want to decode : ")
    secret_text = Steganography.decode(output_path)
    # decode method of Steganography library will retrieve hidden secrete message in selected image
    print("your recieved text is: " + secret_text )
    new_chat = ChatMessage(secret_text, True)  # calling Chat class
    friends[sender].chats.append(new_chat)  # appending in chats in friends list
    