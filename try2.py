import csv
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
# list stores friend of a spy
friends = []

with open('friends.csv', 'rU') as friends_data:
    reader = csv.reader(friends_data)
    for row in reader:
        spy = Spy(name=row[0], age=int(row[1]), experience=int(row[2]), rating=float(row[3]))
        friends.append(spy)
for i in range(len(friends)):
    print("name is" + friends[i].name)
