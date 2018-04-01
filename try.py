from datetime import datetime
friend = []
new_friend = {
    'name': '',
    'chats' : ''
}

new_friend = {
'name': 'pankhi',
'chats':{}

}
friend.append(new_friend)

sender=0
new_chat = {
    "message": "hey",
    "time": datetime.now(),
    "sent_by_me": False
  }

friend[sender]['chats']=new_chat

print (friend[sender]['chats']['message'])


