from datetime import datetime

# data structure to hold list of spy's statuses
status_messages = []

# function add and update status of spy
def spy_status(user):
    current_status_message = None
    show_menu=True
    while(show_menu):
        # menu_choices
        print("What do you want to do? \n1.Add \ update status \n2.close application")
        menu_choice = int(raw_input("enter your choice: "))
        if menu_choice == 1:
            print("you choose to add a status")
            current_status_message=add_status(current_status_message)
            # user[0] is name of current spy
            print(user[0]+" status is : "+current_status_message)
        else:
            show_menu = False

def add_status(current_status_message):

    # user already have a status
    if current_status_message != None:
        print("your current status message is: "+current_status_message)
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

# data structure to hold friend info of spy
friends = []
new_friend = {
    'name': '',
    'age': 0,
    'rating': 0.0,
    'chats' : ''
}


def add_friend(user):

    # details of friend
    new_friend['name'] = raw_input("enter your friend's name: ")
    f_salu = raw_input(new_friend['name']+"'s salutation? ")
    new_friend['name'] = f_salu + "." + new_friend['name']
    new_friend['age'] = int(raw_input("age? "))
    new_friend['rating'] = float(raw_input("spy rating?"))
    new_friend['is_online'] = raw_input("online status(online/offline)? ")

    # user[1] is rating of current spy
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] > user[1]:
        friends.append(new_friend.copy())
        print(new_friend['name']+" added successfully as your friend")
    else:
        print("sorry! invalid entry. We can't add spy with details you provided")

    # return no of friend spy have
    return len(friends)

# it will select a friend out of list of friends
def select_a_friend():
    i = 0
    # displaying list of friends of user
    print("list of your friends:")
    for friend in friends:
        i = i + 1
        print("%d.%s" % (i, friend['name']))
    index = int(raw_input("enter serial.no of friend you want to select "))
    # index will store index no of selected friend in friends list
    return index - 1

# ------------------- steganography -------------------------

from steganography.steganography import Steganography

def send_a_message():
    print("which friend you want to communicate with?")
    selected_friend = select_a_friend()
    # selected_friend contains index of friend selected via select_a_friend function
    print("you want to message %s with rating %.2f"%(friends[selected_friend]['name'], friends[selected_friend]['rating']))
    original_image = raw_input("enter name of image you want to encode secret message with: ")
    output_path = 'output.jpg'
    text = raw_input("enter secret message you want to hide: ")
    Steganography.encode(original_image, output_path, text)
    # encode method of Steganography library will hide secrete message in selected image

    # new_chat dictionary will keep record of all the chats of user
    new_chat = {
        'message' : text,
        'time' : datetime.now,
        'message_by_me' : True
    }
    friends[selected_friend]['chats'] = new_chat
    # chats is a key of dictionary friend in list friends
    print (friends[selected_friend]['chats'])
    print("your secret message is ready")

def read_a_message():
    sender = select_a_friend()
    # sender stores index of friend whose message user want to read
    output_path = raw_input("enter the name of the image you want to decode : ")
    secret_text = Steganography.decode(output_path)
    # decode method of Steganography library will retrieve hidden secrete message in selected image
    print("your recieved text is: " + secret_text )

    # new_chat dictionary will keep record of all the chats of user
    new_chat = {
        'message': secret_text,
        'time': datetime.now,
        'message_by_me': False
    }
    friends[sender]['chats'] = new_chat
    print("your secret message is : "+friends[sender]['chats']['message'])