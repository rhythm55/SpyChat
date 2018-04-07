





import csv
from spy_details import Spy,friends

with open("friends.csv", 'rb') as f_data:
    reader = csv.reader(f_data)
    for row in reader:
        spy = Spy(name=row[0], age=int(row[1]), experience=int(row[2]), rating=float(row[3]))
        friends.append(spy)

for i in range(len(friends)):
    print("name is " + friends[i].name + "age is " + friends[i].age)