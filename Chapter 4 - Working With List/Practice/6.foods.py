# Copying a List
my_foods = ['pizza','falafel','carrot cake']
friends_food = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

'''
To prove that we actually have two separate lists, we’ll add a new food
to each list and show that each list keeps track of the appropriate person’s
favorite foods

'''
my_foods.append('cannoli')
friends_food.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)