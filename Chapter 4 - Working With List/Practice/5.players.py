players = ['charles','martina','michael','florence','eil']
print(players[0:3])
print(players[1:4])
# omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])
# Python returns all items from the third item through the end of the list
print(players[2:])
# last three player
print(players[-3:])
# Looping Through a Slice
print("Here are the first three players on  my team:")
for player in players[:3]: #Instead of looping through the entire list of players at u, Python loops through only the first three names:
    print(player.title())
