class Spy:
    def __init__(self, name, salutation, age, experience, rating):
        self.name = name + salutation
        self.age = age
        self.experience = experience
        self.rating = rating

spy = Spy('rhythm', 'Ms', 21, 3, 4)
li = []
li.append(spy)
print li(spy)