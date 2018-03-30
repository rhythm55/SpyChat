friends = []
new_friend = {
    'name': '',
    'age': 0
}

new_friend['name']=input("name")
new_friend['age']= input("age")
friends.append(new_friend.copy())

new_friend['name']=input("name")
new_friend['age']= input("age")
friends.append(new_friend.copy())

i=0
for friend in friends:
    i=i+1
    print("%d.%s"%(i,friend['name']))


