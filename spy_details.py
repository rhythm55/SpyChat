from datetime import datetime

# details of a spy
class Spy:
        def __init__(self, name, salutation, age, experience, rating):
            self.name = salutation + name
            self.age = age
            self.experience = experience
            self.rating = rating
            self.is_online = True
            self.chats = []
            self.current_status_message = None
            print("%s %d year old with a handful experience of %d years and a rating of %.2f" % (name, age, experience, rating))


class ChatMessage:
        def __init__(self, message, sent_by_me):
            self.message = message
            self.time = datetime.now()
            self.sent_by_me = sent_by_me



friends = []
