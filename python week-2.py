
1.	Write a Python program that defines a Car class with attributes like make, model, and year, and methods like start() to start the car and stop() to stop it.
class Car:
    def __init__(self, make, model, year):  # Corrected constructor name
        self.make = make
        self.model = model
        self.year = year
        self.is_started = False  # To keep track of the car's state

    def start(self):
        if not self.is_started:
            print(f"The {self.year} {self.make} {self.model} is starting.")
            self.is_started = True
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_started:
            print(f"The {self.year} {self.make} {self.model} is stopping.")
            self.is_started = False
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

# Demonstrating the Car class
print("--- Car Class Demonstration ---")
my_car = Car("Toyota", "Camry", 2022)
print(f"My car: {my_car.make} {my_car.model} ({my_car.year})")

my_car.start()
my_car.start()  # Trying to start again
my_car.stop()
my_car.stop()   # Trying to stop again



2.	Write a Python program that demonstrates inheritance by creating a base class Animal and derived classes like Dog, Cat, etc., each with their specific behaviors.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Derived class Dog
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Derived class Cat
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

# Create objects
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

# Common behaviors from Animal class
dog1.eat()
dog1.sleep()

cat1.eat()
cat1.sleep()

# Specific behaviors
dog1.bark()
cat1.meow()

2.4) Write a Python program that demonstrates error handling using the try-except block to handle division by zero.
def safe_divide(numerator, denominator):
    try:
        # Try to divide
        result = numerator / denominator
        print(f"The result of {numerator} / {denominator} is: {result}")
    except ZeroDivisionError:
        # Handle division by zero
        print(f"Error: Cannot divide by zero! Attempted {numerator} / {denominator}")
    except TypeError:
        # Handle wrong data types (e.g., string)
        print("Error: Invalid input types. Please provide numbers.")
    
# Demonstrating error handling
print("\n--- Error Handling Demonstration ---")
safe_divide(10, 2)       # Correct
safe_divide(10, 0)       # Division by zero
safe_divide(5, "abc")    # Type error



2.3) Define a base class called Animal with a method make_sound(). Implement derived classes like Dog. Cat, and Bird that override the make_sound() method to produce different sounds. Demonstrate polymorphism by calling the method on objects of different classes.


class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method 'make_sound'")

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp! Chirp!"

# Demonstrating polymorphism
print("\n--- Polymorphism Demonstration ---")
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(f"An animal makes sound: {animal.make_sound()}")



