# details of a spy
def spy(user):
    # details of default spy
    if user == 'default':
        spy_name = "Ms.rhythm"
        spy_age = 20
        spy_experience = 5
        spy_rating = 4.7

    # fetching details from new spy
    else:
        spy_name = input("Enter your spy name: ")
        if len(spy_name) > 0:
            spy_salutation = input("what should we call you " + spy_name + " (Mr. or Ms.)? ")
            spy_name = spy_salutation + "." + spy_name
            print("Glad to have you here " + spy_name)
            print(
                "Alright " + spy_name + " We would like to know a little bit more about you...")

            # checking weather age of spy is valid or not
            spy_age = int(input("what is your age? "))
            if spy_age < 18 or spy_age > 60:
                print("sorry! your age is not valid to be a spy")
                exit()
            else:
                spy_experience = int(input("for how many years you are working as a spy? "))
                spy_rating = float(input("what is your rating(out of 5)? "))

                # comments according to the rating of spy
                if spy_rating >= 4.5:
                    print("good ace!")
                elif spy_rating < 4.5 and spy_rating >= 3.5:
                    print("you are one of good ones!")
                elif spy_rating < 3.5 and spy_rating >= 2.5:
                    print("you can always do better!")
                else:
                    print("we can always you somebody to help in the office")

                print("thanks for telling the information about you...")

        else:
            print("please enter a valid name")
            # call spy() so that user can input correct name
            spy(user)

    # displaying details of default/new spy
    print("%s %d year old with a handful experience of %d years and a rating of %.2f" % (spy_name, spy_age, spy_experience, spy_rating))
    return spy_name, spy_rating

