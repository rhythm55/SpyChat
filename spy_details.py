# details of a spy
def spy(user):
    # details of default spy
    if user == 'default':
        spy = {
            'name': 'Ms.rhythm',
            'age': 20,
            'experience': 5,
            'rating': 4.7
             }

    # fetching details from new spy
    else:
        spy = {}
        spy['name'] = raw_input("Enter your spy name: ")
        if len(spy['name']) > 0:
            spy_salutation = raw_input("what should we call you " + spy['name'] + " (Mr. or Ms.)? ")
            spy['name'] = spy_salutation + "." + spy['name']
            print("Glad to have you here " + spy['name'])
            print("Alright " + spy['name'] + " We would like to know a little bit more about you...")

            # checking weather age of spy is valid or not
            spy['age'] = int(raw_input("what is your age? "))
            if spy['age'] < 18 or spy['age'] > 60:
                print("sorry! your age is not valid to be a spy")
                exit()
            else:
                spy['experience'] = int(raw_input("for how many years you are working as a spy? "))
                spy['rating'] = float(raw_input("what is your rating(out of 5)? "))

                # comments according to the rating of spy
                if spy['rating'] >= 4.5:
                    print("good ace!")
                elif spy['rating'] < 4.5 and spy['rating'] >= 3.5:
                    print("you are one of good ones!")
                elif spy['rating'] < 3.5 and spy['rating'] >= 2.5:
                    print("you can always do better!")
                else:
                    print("we can always you somebody to help in the office")

                print("thanks for telling the information about you...")

        else:
            print("please enter a valid name")
            # call spy() so that user can input correct name
            spy(user)

    # displaying details of default/new spy
    print("%s %d year old with a handful experience of %d years and a rating of %.2f" % (spy['name'], spy['age'], spy['experience'], spy['rating']))
    return spy['name'], spy['rating']

