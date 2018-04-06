from termcolor import colored

# details of a spy
class Spy:
        def __init__(self, name, age, experience, rating):
            self.name = name
            self.age = age
            self.experience = experience
            self.rating = rating
            self.is_online = True
            self.chats = []
            self.current_status_message = None

        def display_info(self, name, age, experience, rating):
            print colored("%s %d year old with a handful experience of %d years and a rating of %.2f" % (name, age, experience, rating),"blue")

# chats between spies
class ChatMessage:
        def __init__(self, spy_name, friend_name, time, message):
            self.spy_name = spy_name
            self.friend_name = friend_name
            self.time = time
            self.message = message

friends = []
# list stores friend of a spy

chats = []
# list store chats between a spy and his/her friends