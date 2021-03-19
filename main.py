# class Dog():
#
#     def __init__(self, dogbreed, dogheight):
#         self.breed = dogbreed
#         self.height = dogheight
#
#
# my_dog = Dog
#
# test = my_dog.breed='4'
# test2 =my_dog.height="cat"
#
# print(test, test2)


# class Dog():
#     # define a class object attributes. these are attributes that are the same for any instance of the attribute
#     # usually defined above the init method
#     species = 'mammal'
#
#     # the init method must always be defined first
#     def __init__(self, name, breed):
#         self.breed = breed
#         self.name = name
#         self.height = 2
#
#     # method is a function that is inside a class. It ususally works on an instance of the class like below
#     def bark(self):
#         print(f"woof. My name is {self.name}")
#
#
# my_dog = Dog('jack', 'lab')
# #my_dog = Dog()
#
# test = my_dog.name
#
# test1 = my_dog.breed
#
# print(test, test1)
# print(my_dog.height)
# my_dog.bark()
#
#
#
# class Circle():
#     #class object attribute
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     # Method
#     def get_circumference(self):
#         return self.radius * self.pi * 2
#
# my_circle = Circle(30)
#
#
# print(my_circle.radius)
#
# print(my_circle.get_circumference())


#
#
# # Inheritance. This means calling a previously defined class in another class which gives you access to all its attributes
#
# class Animal():
#
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def who_am_i(self):
#         print("I am an animal")
#
#     def eat(self):
#         print("I am eating")
#
# # We can now create another class and call the above class in it to use the attributes
#
# class Cat():
#
#     # first initialise the class of cats
#     def __init__(self):
#
#         # Now initialse the external class you want to call
#         Animal.__init__(self)
#         print("Dog created")
#             # Now you can access all the class methods
#
#
#     # You can also create other methods
#     def meow(self):
#         print("meooooww")
#
# my_cat = Cat()
# #
# # my_cat.meow()
#
#
# def solution(number):
#     num = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             num += i
#         elif i < 0:
#             return "o"
#     else:
#         return num
#
#
# print(solution(10))
#
#
# class Cylinder:
#
#     pi = 3.14
#
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         return Cylinder.pi * self.radius**2 * self.height
#
#     def surface_area(self):
#         return 2 * Cylinder.pi * self.radius * self.height + 2 * Cylinder.pi * self.radius**2
#
#
#
# my_cylinder = Cylinder(2, 3)
#
# print(my_cylinder.volume())
# print(my_cylinder.surface_area())


#     # Method
#     def get_circumference(self):
#         return self.radius * self.pi * 2


# class Dog():
#     # define a class object attributes. these are attributes that are the same for any instance of the attribute
#     # usually defined above the init method
#     species = 'mammal'
#
#     # the init method must always be defined first
#     def __init__(self, name, breed):
#         self.breed = breed
#         self.name = name
#         self.height = 2
#
#     # method is a function that is inside a class. It ususally works on an instance of the class like below
#     def bark(self):
#         print(f"woof. My name is {self.name}")


# how to use help
# print(dir(help()))  # this prints instructions for using help


# magic methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # use special method below to allow you use print in your method.
    # without the special method it will only print out the object representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


b = Book('Thank you Father for your help!!', 'grateful', 1000000)

# print(len(b))
import cmath


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        dis = ((self.coor1[0] - self.coor2[0]) ** 2 + (self.coor1[1] - self.coor2[1]) ** 2) ** 0.5
        return dis

    def slope(self):
        # return (self.coor1[0] - self.coor2[1]) / (self.coor1[1] - self.coor2[1])

        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

    def __str__(self):
        return f"{self.distance()}, {self.slope()}"


l = Line((3, 2), (8, 10))


# print(l)


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"we just added {self.balance} to your account")

    def withdraw(self, withdrawamount):
        if withdrawamount > self.balance:
            print("Sorry insufficient funds")
        elif withdrawamount <= self.balance:
            self.balance -= withdrawamount
            print(f"You withdrew {withdrawamount}. You now have a balance of {self.balance}")

    def __str__(self):
        return f"{self.owner}, {self.balance()}"


acct1 = Account('manny', 0)

acct1.deposit(1000)
acct1.withdraw(5000)

print(acct1.owner, acct1.balance)
