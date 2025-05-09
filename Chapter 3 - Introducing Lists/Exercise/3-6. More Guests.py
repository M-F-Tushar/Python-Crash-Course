invite_dead = ['Uncle', 'Grandfather', 'Grandmother']

print(f"I welcome you to for a dinner {invite_dead[0]}")

print(f"I welcome you to for a dinner {invite_dead[1]}")

print(f"I welcome you to for a dinner {invite_dead[2]}")

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