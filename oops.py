# class Car:
#    def__init__(self,brand,color):
#       self.brand=brand
#       self.color = color
    

#     def start(self):
#         print(f"{self.color}{self.brand}is starting")

# car1 = Car("tesla", "red")
# car2 = Car("BMW", "Black")


# car1.start()
# car2.start()



# the__init__() method (constructor)

# class Student:
#     def __init__(self,name,roll):
#      self.name = name
#      self.roll = roll

# s1 = Student("Alice", 100)
# print(s1.name,s1.roll)




# class Animal:
#     def speak(self):
#         print("Anumal make sounds")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks!")


# d = Dog()
# d.speak()
# d.bark()




# class Animal:
#     def sound(self):
#         print("Some generic sound")

# class Cat(Animal):
#     def bark(self):
#         print("Dog barks!")

# a = Animal
# c = Cat()
# a.speak()
# c.bark()



# class Student:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll

# s1 = Student("Mohit", 18)
# print(s1.name,s1.roll)


# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         print("Area of rectangle:", self.length * self.breadth)



# r = Rectangle(10, 4)
# r.area()


# class Person:
#    def display(self):
#       print("hello person!")

# p = Person()
# p.display()


# class Car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price


#         def start (self):
#             print(f"{self.brand}{self.price} is starting")

# car1 = Car("tesla", 4200000)
# car2 = Car("BMW-M5", 300000000)


# car1.start()
# car2.start()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no



s = Student("Mohit", 19, 101)

print("Name:", s.name)
print("Age:", s.age)
print("Roll No:", s.roll_no)
