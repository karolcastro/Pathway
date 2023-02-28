friends = []

new_friends = ""

while new_friends != "end":
    new_friends = input("Type the name of a friend, type end when finished. ")
    
    if new_friends != "end":
        friends.append(new_friends)
print()
print(f"Your friends are:")

    
for friend in friends:
    print(friend.title())