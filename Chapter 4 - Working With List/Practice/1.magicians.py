magicians =["Alice", "David", "Carolina"]
for magician in magicians: #For every magician in the list of magicians, print the magician’s name
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


print("Thank you, everyone. That was a great magic show")