from termcolor import colored

# details of a spy
class Spy:
    def __init__(self, name, password, age, experience, rating):
        self.name = name
        self.password = password
        self.age = age
        self.experience = experience
        self.rating = rating
        self.current_status_message = None
    # to display details of the spy
    def display(spy):
        print colored("%s %d year old with a handful experience of %d years and a rating of %.2f" % (spy.name, spy.age, spy.experience, spy.rating), "blue")

# details of friend and name of person who's friend are they
class Friend:
        def __init__(self, friend_of, name, experience, rating):
            self.friend_of = friend_of
            self.name = name
            self.experience = experience
            self.rating = rating

# chats between spies
class ChatMessage:
        def __init__(self, sent_by_me, friend_name, time, message):
            self.sent_by_me = sent_by_me
            self.friend_name = friend_name
            self.time = time
            self.message = message

# list stores friend of a spy
friends = []

# list store chats between a spy and his/her friends
chats = []
