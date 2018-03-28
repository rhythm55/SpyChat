def default_spy():
    spy_name = "rhythm"
    spy_salutation = "Ms"
    spy_age = 20
    spy_experience = 5
    spy_rating = 4.7
    detail(spy_name, spy_salutation, spy_age, spy_experience, spy_rating)

# detail function is to display details of a spy
def detail(spy_name, spy_salutation, spy_age, spy_experience, spy_rating):
    # print("%s.%s %d year old with a handful experience of %d years and a rating of %.2f" % (spy_salutation,spy_name,spy_age,spy_experience,spy_rating))
    spy_name = spy_name + spy_salutation
    return (spy_name)

# spy_active = default_spy()
# print(spy_active)
default_spy()