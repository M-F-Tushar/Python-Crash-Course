invite_dead = ['Uncle', 'Grandfather', 'Grandmother']

print(f"I welcome you to for a dinner {invite_dead[0]}")

print(f"I welcome you to for a dinner {invite_dead[1]}")

print(f"I welcome you to for a dinner {invite_dead[2]}")

number = len(invite_dead)

print(f"The number of poeple invited in the dinner {number}") 

unable_to_come = invite_dead.pop()

print(f"Unfortunately {unable_to_come} is unable to come")

invite_dead.append("Second Uncle")

print(f"I welcome you to for a dinner {invite_dead[0]}")

print(f"I welcome you to for a dinner {invite_dead[1]}")

print(f"I welcome you to for a dinner {invite_dead[2]}")

print("I found a bigger dinner table, so now i can invite more people")

invite_dead.insert(0,"Third Uncle")
invite_dead.insert(2,"Grandmother")
invite_dead.append("Aunty")

print(invite_dead)

print("I am sorry, but i can only invite two people")

unable_to_invite = invite_dead.pop()

print(f"Sorry, I am unable to invite you {unable_to_invite}")

unable_to_invite = invite_dead.pop()

print(f"Sorry, I am unable to invite you {unable_to_invite}")

unable_to_invite = invite_dead.pop()

print(f"Sorry, I am unable to invite you {unable_to_invite}")

unable_to_invite = invite_dead.pop()

print(f"Sorry, I am unable to invite you {unable_to_invite}")

print(f"But you are still invited {invite_dead[0]}")

print(f"But you are still invited {invite_dead[1]}")

del invite_dead[0]
del invite_dead[0]

print(invite_dead)

number = len(invite_dead)

print(f"The number of poeple invited in the dinner {number}")
