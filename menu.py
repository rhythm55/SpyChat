import os
import csv
from spy_details import Spy,friends,ChatMessage,chats
from datetime import datetime
from termcolor import colored
from steganography.steganography import Steganography

# data structure to hold list of spy's statuses
status_messages = ["at work", "busy don't disturb"]

# function add and update status of spy
def spy_status(spy):
    current_status_message = None
    show_menu = True
    while(show_menu):
        # menu_choices
        print("What do you want to do? \n1.Add \ update status \n2.close application")
        menu_choice = int(raw_input(colored("enter your choice: ", "yellow")))
        if menu_choice == 1:
            print(colored("you choose to add a status", "blue"))
            spy.current_status_message = add_status(spy.current_status_message)
            print colored(spy.name + " status is : " + spy.current_status_message, "magenta")
        else:
            show_menu = False

def add_status(current_status_message):

    # user already have a status
    if current_status_message != None:
        print colored("your current status message is: " + current_status_message, "magenta")
        default = raw_input(colored("Do you want to select from the older status (Y/N)? ", "yellow"))
        # user want to add new status
        if default.upper() == 'N':
            new_status_message = raw_input(colored("what status message you want to set? \n", "yellow"))
            if len(new_status_message) > 0:
                status_messages.append(new_status_message)
                current_status_message=new_status_message
            else:
                print colored("invalid status message", "red")
                spy_status()
        # user wants to select status from list of old statuses
        else:
            print colored("select which old status you want as your current status? ", "yellow")
            item_position = 1
            for message in status_messages:
                print colored(str(item_position)+"."+message, "blue")
                item_position = item_position+1
            message_selection = int(raw_input(colored("\n choose from above messages:", "yellow")))
            if message_selection > 0:
                current_status_message=status_messages[message_selection-1]

    # user do not have any status yet
    else:
        print colored("you don't have any status message currently! ", "red")
        new_status_message = raw_input(colored("enter a status message : \n", "yellow"))
        if len(new_status_message) > 0:
            current_status_message = new_status_message
            status_messages.append(current_status_message)
        else:
            print colored("invalid status message", "red")
            spy_status()

    # function will return current message updated from cases accordingly
    return current_status_message

def add_friend(spy):

    # details of friend
    name = raw_input("enter your friend's name: ")
    salutation = raw_input(name + "'s salutation? ")
    name = salutation + "." + name
    age = int(raw_input("age? "))
    experience = int(raw_input("experience ?"))
    rating = float(raw_input("spy rating?"))

    if len(name) > 0 and age > 12 and age < 65 and rating > spy.rating:
        new_friend = Spy(name, age, experience, rating)
        # friend is appended in friends list
        friends.append(new_friend)
        # the spy's friend is added in friends.csv
        with open('friends.csv','a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([name, age, experience, rating])
        print colored(name+" added successfully as your friend", "green")
    else:
        print colored("sorry! invalid entry. We can't add spy with details you provided", "red")

    # return no of friend spy have
    return len(friends)

# it will select a friend out of list of friends
def select_a_friend():
    # displaying list of friends of user
    print colored("list of your friends:", "blue")
    item_number = 0
    for f in range(0, len(friends)):
            item_number += 1
            print colored('%d. %s %d year old with rating %.2f' % (item_number, friends[f].name, friends[f].age, friends[f].rating), "magenta")
    index = int(raw_input(colored("enter serial.no of friend you want to select ", "yellow")))
    # index will store index no of selected friend in friends list
    return index - 1

# ------------------- steganography -------------------------

special_text = ['SAVE ME', 'DANGER', 'HELP ME', 'SOS']
# if words in special_text list are used during send message a special message is sent to receiver
# if words in spcial_text list are while reading a message a special message output is displayed

def send_a_message(spy):
    print colored("which friend you want to communicate with?", "yellow")
    selected_friend = friends[select_a_friend()].name
    # selected_friend contains index of friend selected via select_a_friend function
    original_image = raw_input(colored("enter name of image you want to encode secret message with(.jpg format): ", "yellow"))
    # checking if mentioned file exist in os or not
    if os.path.exists(original_image):
        # checking extension of image if its in jpg
        if os.path.splitext(original_image)[1] == ".jpg":
            output_path = 'output.jpg'
            text = raw_input(colored("enter secret message you want to hide: ", "yellow"))
            if text in special_text:
                text = colored(text + ": its a emergency reach me as soon as possible!!", "red", attrs=['bold'])
            # encode method of Steganography library will hide secrete message in selected image
            Steganography.encode(original_image, output_path, text)
            # storing chats in chatmessage
            chat = ChatMessage(spy_name=spy.name, friend_name=selected_friend, time=datetime.now().strftime("%d %B %Y"), message=text)
            chats.append(chat)
            # writing chats in chats.csv
            with open("chats.csv", 'a') as chat_record:
                writer = csv.writer(chat_record)
                writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])
            print colored("your secret message is ready", "blue")
        else:
            print colored("file not in .jpg format", "red")
    else:
        print colored("file does not exist", "red")

def read_a_message(spy):
    sender = friends[select_a_friend()].name
    # sender stores index of friend whose message user want to read
    output_path = raw_input(colored("enter the name of the image you want to decode(.jpg format) : ", "yellow"))
    # checking if mentioned file exist in os or not
    if os.path.exists(output_path):
        # checking extension of image if its in jpg
        if os.path.splitext(output_path)[1] == ".jpg":
            text = Steganography.decode(output_path)
            # decode method of Steganography library will retrieve hidden secrete message in selected image
            print colored("your received text: " + text , "blue")
            if text in special_text:
                print colored("don't worry " + sender + "on the way to rescue you!!!", "green", attrs=['bold'])
            # storing chats in chatmessage
            chat = ChatMessage(spy_name=spy.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"), message=text)
            chats.append(chat)
            # writing chats in chats.csv
            with open("chats.csv", 'a') as chat_record:
                writer = csv.writer(chat_record)
                writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])
        else:
            print colored("file not in .jpg format", "red")
    else:
        print colored("file does not exist", "red")

# it will display chats of the current spy with his/her friend
def read_chat(spy):
    print colored("with which friend you want to read chat?", "yellow")
    selected_friend = friends[select_a_friend()].name
    # reading chats from chats.csv
    with open("chats.csv", 'rU') as chat:
        reader = csv.reader(chat)
        for row in reader:
            try:
                c = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                # checking the chats of the current spy with selected friend
                if c.spy_name == spy.name and c.friend_name == selected_friend:
                    print colored("You sent message to %s on [%s] : %s"%(selected_friend, c.time, c.message), "blue")
                    return 1
            except IndexError:
                pass
            continue


