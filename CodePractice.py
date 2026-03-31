# if else elif condition practice

# marks = int(input("Enter student marks: "))
# if marks>=90:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>= 60:
#     grade = "C"
# elif marks>= 45:
#     grade = "D"
# else:
#     grade = "FAIL"
# print(("marks: ", marks),("grade: ", grade))

# a = 1001
# for i in range(a):
#         if i % 2 == 0:
#             print(i)



'''num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, "x", i, "=", num * i)'''


'''num = int(input("Enter a n"umber: "))
for i in range(1,21):
    print(num,'x',i,'=',num*i)'''


#Loops and statement:
#Loops allow to execute a block of code repeatedly based on a condition.
#break, continue, and else statements can be used within loops to control their behavior.


#for loop:
#
# # Using a for loop to iterate over a list
# '''fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)'''
# #while loop:

# Using a while loop to print numbers 1 to 5
# count = 1
# while count <= 5:
#     print(count)
#     count += 1  # Increment count
#
# #break stmt:
#
# # Using break to exit a loop
# for num in range(10):
#     if num == 5:
#         break
#     print(num)


#Continue stmt:

# Using continue to skip even numbers
# for num in range(10):
#     if num % 2 == 0:
#         continue
#     print(num)

#if Statement:

#if statement evaluates a condition and executes the block of code if the condition is True.

# x = 20
# if x > 5:
#     print("x is greater than 5")


#else Statement:

#else statement can be used after an if statement to define a block of code that will execute if the condition is False.


# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is 5 or less")


#elif Statement:

#The elif (short for "else if") allows you to check multiple conditions. If the first if condition is False,
# the program checks the elif conditions sequentially.
# x = 7
# if x > 10:
#     print("x is greater than 10")
# elif x > 5:
#     print("x is greater than 5 but less than or equal to 10")
# else:
#     print("x is 5 or less")


#####################################################
'''stored_pin = 1234
balance = 1000


pin = int(input("Enter your PIN:"))


if pin == stored_pin:
   print("Login successful")
   print("1.Check balance")
   print("2.Withdraw money")
   print("3.Deposit Money")
   print("4.Exit")


   choice =int(input("Enter your choice:"))
   if choice == 1:
       print(balance)


   elif choice == 2:
     amount = int(input("Enter the amount:"))


     if amount<=balance:
        balance=balance-amount
        print("Please collect your cash")
        print("\nRemaining balance is", balance)
     else:
       print("insufficient balance")


   elif choice == 3:
       deposit = int(input("Enter your amount:"))
       balance = balance+deposit
       print("Amount is credited successfully")
       print("Updated balance is", balance)


   elif choice == 4:
       print("Thank you for using ATM")
   else:
       print("Invalid option")
else:
   print("Incorrect PIN.")
'''
#List examples
# a = [10, 20, 30, 40, 50,50,50]
# b = []
#
# for i in a:
#    if i not in b:
#        b.append(i)
# print(b)

#   ===========================================Test QUESTION:=======================================
# Remove duplicate elements from a tuple.
# Concatenate two tuples.
# Find the length of a given tuple.
# Find the sum of all elements in a tuple.
# Count the frequency of characters in a string using a dictionary.
# Remove duplicate values from a dictionary.
# Convert a dictionary into a list of tuples.


# Remove duplicate elements from a tuple
# tuple = (1, 2, 3, 2, 4, 1, 5)
# result = ()
# for i in tuple:
#     duplicate = 0
#     for x in result:
#         if i == x:
#             duplicate = 1
#             break
#     if duplicate == 0:
#         result = result + (i,)
# print(result)

# Concatenate two tuples.

# t1 = (1,2,3,4,5,6,7,8,9)
# t2 = (10,20,30,40,50,60,70)
# result = ()
# for i in t1:
#     result = result + (i,)
# for i in t2:
#     result = result + (i,)
# print(result)


# Find the length of a given tuple----------------------------------------

# t1 = (1,2,3,4,5,6,7,8,9)
# t = (10, 20, 30, 40, 50)
# count = 0
# for i in t:
#     count = count + 1
# print(count)

# Find the sum of all elements in a tuple.-----------------------------------------
# t1 = (1,2,3,4,5,6,7,8,9,10,15)
# total = 0
#
# for i in t1:
#     total = total + i
#
# print(total)

#Count the frequency of characters in a string using a dictionary.

# R = "RocketScience"
# frequency = {}
#
# for T in R :
#     if T in frequency:
#         frequency[T] += 1
#     else:
#         frequency[T] = 1
#
# print(frequency)

## Remove duplicate values from a dictionary.
# dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'b':2, 'c':3, 'd':4}
# dict2 = {}
# for K,V in dict1.items():
#     if K not in dict2:
#         dict2[K] = V
# print(dict1)
# print(dict2)

##Convert a dictionary into a list of tuples.

# dict ={'a' : 1, 'b' :2, 'c' :3, 'd' : 4 }
# print(list(dict.items()))


# a = {2: 'python', 3: 'java', 4: 'trainer', 5: 'code'}
# for x in a.items():
#     print(x)


#----------# Remove duplicate values from a dictionary.----------------#
# A = {'a': 1, 'b': 2, 'c': 1, 'd': 3} # dictionary
# result = {}   #--empty dict to store new Key:Value
#
# for k, v in d.items(): # d.items() will check the key value pair in dictionary.
#     if v not in result.values(): # this will check the key values present or not in result  dict , if not add, if yes jump
#                                     result.value() will check the key values in result dictionary.
#         result[k] = v   # this line will add key with value in result dictionary.
#
# print(result) #------# here finally printing the new dictionary.

#----------------#------------ functions------------------#
# def is function in python, function is block of code to execute the task, inside the functions methods we can write
# we can reuse the code of class,functions.

# Syntax:
# def function_name(parameters):
#       return result

# Program:

# def add_numbers(a, b):
#     return a + b
#
# result = add_numbers(5, 3)
# print(result)
#
#
# Parameters: Variables listed in the function's definition (a and b).
#
# Arguments: Values passed to the function when you call it (5 and 3).

# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5, 3)
# print(result)

# OOPS, concept: (Object-Oriented Programming System)
#
# Object-Oriented Programming (OOP) in Python is a programming based on the concept of objects.
#
# These objects are instances of classes, which can contain both data (attributes) and methods (functions).
#
# OOP is designed to enhance code reusability, modularity, and maintainability.
#
# Classes and Objects:
# class Person:
#     def __init__(self, name, age): # constructor
#         self.name = name  # Public Attribute
#         self.__age = __age  # Private
#
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.") # format string
#
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
# person3 = Person("rev",10)
#
# person1.greet()
# person2.greet()
# person3.greet()


# Encapsulation:
#
# - Encapsulation is the concept of hiding the internal details of an object and only exposing necessary parts through controlled access.
#
# - It helps in data security and prevents accidental modification of data.

'''class BankAccount:


   def __init__(self, account_number, balance):
       self.account_number = account_number  # Public attribute
       self.__balance = balance  # Private attribute`
   # private attribute will not be access directly. If we want to access, create a method to access it.


   def deposit(self, amount): # 40000
       self.__balance += amount


   def withdraw(self, amount):
       if amount <= self.__balance:
           self.__balance -= amount
       else:
           print("Insufficient funds!")


   def get_balance(self):  # Public method to access private variable # Getter Method..
       return self.__balance


# Creating an object
account1 = BankAccount("123456", 5000)
account2 = BankAccount("345644",10000)
account3 = BankAccount("34343443434",50000)


account1.deposit(5000)
account1.withdraw(1000)
print("Account 1 Balance is:",account1.get_balance())


account2.deposit(10000)
account2.withdraw(2000)
print("Account 2 Balance is:",account2.get_balance())


account3.deposit(20000)
account3.withdraw(3000)
print("Account 3 Balance is:",account3.get_balance())'''

# Inheritance:
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


# Types of Inheritance:

# Single Inheritance -> Single Parent class, single child class
# Multiple Inheritance -> A child inherits from more than one parent class
# Multilevel Inheritance -> A chain of Inheritance ( Grand Parent, Parent, Child )
# Hierarchical Inheritance -> Multiple child classes inherit from a single parent class
# Hybrid Inheritance -> A combination of 2 or more types of inheritance

#Hierarchical:

# class Vehicle:
#    def __init__(self, make, model, year):
#        self.make = make # instance variable
#        self.model = model
#        self.year = year
#    def display_info(self):
#        return f"{self.year} {self.make} {self.model}"
# # Derived class
# class Car(Vehicle): # inherits
#    def __init__(self, make, model, year, doors):
#        super().__init__(make, model, year)
#        self.doors = doors
#    def display_info(self):
#        return f"{super().display_info()} with {self.doors} doors"
# # Another derived class
# class Motorcycle(Vehicle):
#    def __init__(self, make, model, year, type):
#        super().__init__(make, model, year)
#        self.type = type
#    def display_info(self):
#        return f"{super().display_info()} which is a {self.type} type"
# car = Car("Toyota", "Camry", 2020, 4)
# motorcycle = Motorcycle("Harley Davidson", "Street 750", 2019, "Cruiser")
# print(car.display_info())
# print(motorcycle.display_info())

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Local Variable:
# Local variables are variables that are defined within a function and are only accessible within that function.
# They have a limited scope and are not accessible outside the function in which they are defined.

# def calculate_sum(a, b):
#     result = a + b  # Local variable
#     return result
#
# sum_result = calculate_sum(5, 3)
#
# print(sum_result)

# Input and Output:
# Input and output operations are typically handled using built-in functions.
# input():
#-Used to take input from the user.

# Program:
# a = input("Enter your name: ")
# print(a)
# output()
# print()

# - Used to output data to the console.
# Program using I/O: ( f-strings, .format())

# Getting user input
# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
# # Outputting the information
# print(f"Hello, {name}! You are {age} years old.")

# Validating input
# while True:
#     try:
#         age = int(age)
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         break
#     except ValueError:
#         age = input("Please enter a valid age: ")

# Reading and writing text files:
#  It provides built-in functions for creating, writing, and reading files.
#
# 'r': Read (default mode).
# 'w': Write (overwrites existing).
# 'a': Append (adds to the end).
# 'r+': Read and write (does not truncate the file).

# Syntax:
# map(function, iterable, ...)
# function: A function that takes one or more arguments.
# iterable: One or more iterables (like lists, tuples, etc.) whose elements you want to process
# Program:
# def square(x):
#     return x * x
#
# # A list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Use map() to apply the square function to each number
# squared_numbers = map(square, numbers)
#
# # Convert the map object to a list and print the result
# print(list(squared_numbers))

# Error handling execptions:
#
# Syntax:

#try:
#     # Code that may raise an exception
#     result = 10 / 0  # Example that raises Zero-Division-Error
#
# except ZeroDivisionError:
#     # Handle the specific exception
#     print("Cannot divide by zero!")
#
# except Exception as e:
#     # Handle any other exception
#     print(f"An error occurred: {e}")
#
# else:
#     # This block runs if no exception occurs
#     print(f"The result is {result}")
#
# finally:
#     # This block always runs, regardless of exceptions
#     print("Execution completed.")

