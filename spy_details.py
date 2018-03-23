spy_name = "rhythm"
spy_salutation = "Ms"
spy_age = 20
spy_experience = 5
spy_rating = 4.7

# detail function is to display details of spy
def detail(spy_name, spy_salutation, spy_age, spy_experience, spy_rating):
    print("%s.%s %d year old with a handful experience of %d years and a rating of %.2f" % (spy_salutation,spy_name,spy_age,spy_experience,spy_rating))

def new_spy():
    # fetching details from new spy
    spy_name = input("Enter your spy name: ")
    if len(spy_name) > 0:
        spy_salutation = input("what should we call you " + spy_name + " (Mr. or Ms.)? ")
        print("Glad to have you here " + spy_salutation + "." + spy_name)
        print("Alright " + spy_salutation + "." + spy_name + " We would like to know a little bit more about you...")
        spy_age = int(input("what is your age? "))
        if spy_age < 18 or spy_age > 60:
            print("sorry! your age is not valid to be a spy")
            exit()
        else:
            spy_experience = int(input("for how many years you are working as a spy? "))
            spy_rating = float(input("what is your rating(out of 5)? "))
            if spy_rating >= 4.5:
                print("good ace!")
            elif spy_rating < 4.5 and spy_rating >= 3.5:
                print("you are one of good ones!")
            elif spy_rating < 3.5 and spy_rating >= 2.5:
                print("you can always do better!")
            else:
                print("we can always you somebody to help in the office")
            print("thanks for telling the information about you...")
            detail(spy_name, spy_salutation, spy_age, spy_experience, spy_rating)
    else:
        print("please enter a valid name")
        exit()