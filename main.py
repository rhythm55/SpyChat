print("Welcome to SpyChat")
# fetching details from spy
spy_name=input("Enter your spy name: ")
if len(spy_name) > 0:
    spy_salutation=input("what should we call you "+spy_name+" (Mr. or Ms.)? ")
    print("Glad to have you here " + spy_salutation + "." + spy_name)
    print("Alright " + spy_salutation + "." + spy_name + " We would like to know a little bit more about you...")
    spy_age = int(input("what is your age? "))
    if spy_age < 18 and spy_age > 60:
        print("sorry! your age is not valid to be a spy")
    else:
        spy_experience = input("for how many years you are working as a spy? ")
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
        print("Authentication complete!\n proud to have you on board\n" + spy_salutation + "." + spy_name + "of" + str(
            spy_age) + "years with a handful experience of " + spy_experience + " years and a rating of " + str(spy_rating)
else:
    print("please enter a valid name")
