class Dog:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        
    def sit(self):
        print(f"{self.name} is sitting now")
        
    def roll_over(self):
        print(f"{self.name} rolled over")
    

my_dog = Dog('Buddy', 3)
your_dog = Dog('Lucy', 5)

print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(f"Your dog's name is {your_dog.name} and she is {your_dog.age} years old.")

my_dog.sit()
your_dog.roll_over()