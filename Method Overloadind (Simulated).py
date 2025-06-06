# Method Overloarding (Simulated) -A
Task 1: Define the Printer class with a single method

class Printer:
    def print_message(self, message, times=1):
        for _ in range(times):
            print(message)

# Task 2: Use the Printer class 
if __name__ == "__main__":
    printer = Printer()
    printer.print_message("hello")
    printer.print_message("hello", 3)

# Method Overriding- B
Task 1: Define the Base class Animal 
class Animal:
    def speak(self):
        return "Animal speaks"
    
# Task 2:
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def make_anmial_speak(animal):
    print(animal.speak())

# Task 3: Use the class and Methods
if __name__ == "__main__":
    dog =Dog()
    cat = Cat()
    make_anmial_speak(dog)
    make_anmial_speak(cat)

# Duck Typing-C

Task 1: Define two classes with the same method fly() and define function
class Bird:
    def fly(self):
        return "Flying high"
class Airplane:
    def fly(self):
        return "Flying through the skies"
def let_it_fly(entity):
        print(entity.fly())

# Task 2: Create objects and demonstrate Duck Typing
if __name__ == "__main__":
    bird = Bird()
    airplane = Airplane()

    let_it_fly(bird)
    let_it_fly(airplane)

# Super() Class- D

# Task 1: Defing the class item 
# class item:
#     def __init__(self, name, quantity):
#         self.name = name
#         self.quantity = quantity
#     def display(self):
#         print(f"item: {self.name}, Quantity: {self.quantity}")

# # Task 2: Define the Derived class perishabletlem
# class Perishableltem(item):
#     def __init__(self, name, quantity, expiration_date):
#         super().__init__(name, quantity)
#         self.expiration_date = expiration_date
#     def display(self):
#         super().display()
#         print(f"Expiration Date: {self.expiration_date}")

# # Task 3: non perishableltem
# class NonPerishableitem(item):
#     def display(self):
#         super().display()
#         print("This is a nonperishable item.")

# # Task 4: Instantiate objects and display item details 
# apple = Perishableltem("Apple",10, "2024-10-15")
# canned_beans = NonPerishableitem("Canned Beans",20)
# print("Perishable item details:")
# apple.display()
# print("\nNON_Perishable item details:")
# canned_beans.display
