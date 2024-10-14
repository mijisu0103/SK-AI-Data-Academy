"""Practice 1:

1. Traverse and print each element of the list mylist2 using a loop.
2. Traverse and print each element of the tuple mytuple using a loop.
3. Traverse and print each character of the string mystr using a loop.
4. Press the Submit button to check if you've used loops as instructed."""

mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# To print all values in mylist1:
print(mylist1[0])
print(mylist1[1])
print(mylist1[2])
print('...')
print(mylist1[8])
print(mylist1[9])

# Using for and in to create a loop

# Code based on instruction 1:
mylist2 = [10, 20, 30, 40, 50]
for i in mylist2:
    print(i)

# Code based on instruction 2:
mytuple = ('A', 'B', 'C', 'D', 'E')
for j in mytuple:
    print(j)

# Code based on instruction 3:
mystr = "Hello"
for k in mystr:
    print(k)

""" Mission 1:

Write code according to each instruction, referring to the output result:

  1. Use loops and conditional statements to print only the negative numbers from the list sample.

  Output:
  -20
  -33
  -5
  -9
  -1
  -100

  2. Use loops and conditional statements to print only the elements of sample that are greater than 10 and less than 50.

  Output:
  11
  22
  12
  35
  19"""

sample = [1, 11, 22, -20, 55, -33, 0, -5, 12, 35, 19, -9, -1, -100]

# Code for instruction 1:
for i in sample:
    if i < 0:
        print(i)

# Code for instruction 2:
for j in sample:
    if 10 < j < 50:
        print(j)

""" Practice 2:

1. Use range() to print numbers from 0 to 9.
2. Use range() to print numbers from 2 to 10.
3. Use range() to print only odd numbers from 1 to 9.
4. Think about and experiment with nested loops.
5. Press the Submit button to verify your solution."""

# Code for instruction 1:
for i in range(10):
    print(i)

# Code for instruction 2:
for i in range(2, 11):
    print(i)

# Code for instruction 3:
for i in range(1, 10, 2):
    print(i)

# Code for instruction 4:
for i in range(1, 4):
    for j in range(1, 4):
        print(f'(i={i}) + (j={j}) = {i * j}')
    print('===')

"""Mission 2:

Use a loop to print the multiplication tables (2 to 9) with a blank line between each table. Ensure the output matches the following:

2 X 1 = 2
2 X 2 = 4
...
9 X 9 = 81"""

# Code for printing the multiplication tables:
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i * j}')
    print()

"""Practice 3:

1. Use a loop, a conditional statement, and continue to print only even numbers.
2. Use a loop, a conditional statement, and break to stop the loop when i is 7 or greater.
3. Use a loop, a conditional statement, and break to print numbers from 0 to 4.
4. Use a loop, a conditional statement, and continue to skip 2 and print numbers from 0 to 9."""

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Code for instruction 1:
for i in mylist:
    if i % 2 == 1:
        continue
    print(i)

# Code for instruction 2:
for i in mylist:
    if i >= 7:
        break
    print(i)

# Code for instruction 3:
for i in range(10):
    if i > 4:
        break
    print(i)

# Code for instruction 4:
for i in range(10):
    if i == 2:
        continue
    print(i)

"""Practice 4:

1. Implement a while loop that runs as long as count1 is greater than 0.
2. Use break to exit the while loop when count2 is greater than 5.
3. Press the Submit button to verify your solution."""

# Code for instruction 1:
count1 = 5
while count1 > 0:
    print(count1)
    count1 -= 1

# Code for instruction 2:
count2 = 1
while True:
    print(count2)
    count2 += 1
    if count2 > 5:
        break

"""Mission 3:

Write a while loop to calculate and print the sum of even numbers from 1 to 50.

Output:
count: 2, total: 2
count: 4, total: 6
count: 6, total: 12
...
count: 50, total: 650"""

count = 1
total = 0
while count <= 50:
    if count % 2 == 0:
        total += count
        print(f'count: {count}, total: {total}')
    count += 1
  
"""Practice 5:

Define and call functions based on the given instructions."""

# Instruction 1: Define a function with two parameters and return the result.
def sample_function1(a, b):
    result = a + b
    return result

# Instruction 2: Define a function without parameters, and return the result.
def sample_function2():
    a = 1
    b = 2
    result = a + b
    return result

# Instruction 3: Define a function with parameters but no return value.
def sample_function3(a, b):
    result = a + b
    print(f'result: {result}')

# Instruction 4: Define a function without parameters and without a return value.
def sample_function4():
    print('Hello, World!')

# Verification code
print(sample_function1(1, 3))
print(sample_function2())
sample_function3(1, 7)
sample_function4()

"""Practice 6:

Call functions in different ways and understand the return behavior."""

def sample_function1():
    print('The function is called!')

# Printing only the function name:
print(sample_function1)

# Calling the function:
sample_function1()

# Assigning the function to a variable and calling it:
a = sample_function1
a()

# Function with a return value:
def sample_function2():
    print('The function is called!')
    return 123

result1 = sample_function2()
print(result1)

# Function without a return value:
def sample_function3():
    print('The function is called!')

result2 = sample_function3()
print(result2)

"""Practice 7:

Understanding function arguments: positional arguments, keyword arguments, and default arguments."""

# Using positional arguments:
def add_function1(a, b, c):
    result = a + b + c
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result

add_function1(1, 3, 7)

# Using keyword arguments:
def add_function2(a, b, c):
    result = a + b + c
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result

add_function2(a=5, b=3, c=1)

# Using default arguments:
def add_function3(a, b=0, c=0):
    result = a + b + c
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result

add_function3(1)
add_function3(1, 3)
add_function3(1, 3, 5)
add_function3(c=5, b=3, a=1)

"""Practice 8:

Understanding functions with variable-length arguments (*args).

1. Complete the function add_function1 to accept a variable number of arguments.
2. Complete the function add_function2 to accept a fixed argument a and variable-length arguments."""

# Code for instruction 1:
def add_function1(*args):
    result = 0
    print(f'Type of args: {type(args)}')
    
    for arg in args:
        print(arg)
        result += arg

    print('===' * 5)
    print(f'Sum: {result}')

# Without passing any arguments (this is allowed):
add_function1()

# Passing one argument:
add_function1(1)

# Passing multiple arguments:
add_function1(1, 2, 3, 4, 5)

# Code for instruction 2:
def add_function2(a, *args):
    print(f'a: {a}')
    print('===' * 5)
    
    result = 0
    for arg in args:
        print(arg)
        result += arg
    
    print('===' * 5)
    print(f'Sum: {result}')

# Error due to missing the required argument:
# add_function2()

# Passing one fixed argument:
add_function2(1)

# Passing the fixed argument and multiple variable-length arguments:
add_function2(1, 2, 3, 4, 5)

"""Mission 4:
Write a function that uses variable-length arguments to count the number of elements passed to it.

Output:
The number of passed elements is: 0
The number of passed elements is: 3
The number of passed elements is: 5"""

def count_function(*args):
    print(f'The number of passed elements is: {len(args)}')

# Test code:
count_function()
count_function(1, 2, 3)
count_function(1, 2, 3, 4, 5)

"""Practice 9:

Understanding functions with keyword variable-length arguments (**kwargs).

  1. Complete the function add_function to accept keyword variable-length arguments.
  2. Pass the dictionary person to the add_function."""

# Code for instruction 1:
def add_function(**kwargs):
    total_age = 0
    for name, age in kwargs.items():
        print(f'Name: {name}, Age: {age}')
        total_age += age
    
    print('===' * 5)
    print(f'Total age sum: {total_age}')

# Without passing any keyword arguments:
add_function()

# Passing one keyword argument:
add_function(lee=5)

# Passing multiple keyword arguments:
add_function(john=10, peter=12, lee=5)

# Code for instruction 2:
person = {'john': 10, 'peter': 12, 'lee': 5}
print(person)
add_function(**person)

"""Practice 10:

Understanding lambda (anonymous functions).

1. Define a lambda function that takes parameter x and returns x * 3.
2. Define a lambda function that takes parameters x and y and returns x * y.
3. Define a lambda function that takes parameters x and y with y having a default value of 10, and returns x * y.
4. Define a lambda function that takes parameters x and y and returns x * y if x > 0; otherwise, returns y."""

# Code for instruction 1:
a = lambda x: x * 3
print(a(4))  # Output: 12

# Code for instruction 2:
b = lambda x, y: x * y
print(b(4, 9))  # Output: 36

# Code for instruction 3:
c = lambda x, y=10: x * y
print(c(3))  # Output: 30
print(c(y=5, x=3))  # Output: 15

# Code for instruction 4:
d = lambda x, y: x * y if x > 0 else y
print(d(4, 8))  # Output: 32
print(d(-1, 8))  # Output: 8

# More complex lambda with conditional logic:
e = lambda x: x * 10 if x < 2 else (x**2 if x < 4 else x + 10)
print(e(1))  # Output: 10
print(e(3))  # Output: 9
print(e(4))  # Output: 14

"""Mission 5:

Define a function calc_many that accepts a choice and variable-length arguments. If the choice is 'sum', the function should return the sum of the arguments; if the choice is 'mul', it should return the product.

Output:
10
120"""

def calc_many(choice, *args):
    total = 0
    if choice == 'sum':
        for i in args:
            total += i
    elif choice == 'mul':
        total = 1
        for i in args:
            total *= i
    return total

# Test code:
print(calc_many('sum', 0, 1, 2, 3, 4))  # Output: 10
print(calc_many('mul', 1, 2, 3, 4, 5))  # Output: 120

"""Practice 11:

Packages and Modules

Modules: A .py file that contains Python functions.
Packages: A collection of modules, also known as libraries.

You can import Python modules to use predefined functions."""

import random

# Shuffling a list using the random module:
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)

# Using an alias (shortcut) for the random module:
import random as rd
b = [1, 2, 3, 4, 5]
rd.shuffle(b)
print(b)

# Importing specific functions from a module:
from random import shuffle
c = [1, 2, 3, 4, 5]
shuffle(c)
print(c)

"""Practice 12:
Understanding different ways to import modules.

Commonly used modules for data analysis and visualization:"""

import numpy as np  # Scientific computation
import pandas as pd  # Data manipulation and analysis
import matplotlib.pyplot as plt  # Data visualization library
import seaborn as sns  # Built on top of matplotlib for enhanced data visualization (more attractive and easier-to-use)
import random  # Random number generation

# Example using random module:
import random

a = [1, 2, 3, 4, 5]

#Execute shuffle function in random module
random.shuffle(a)
print(a)

#Importing a module using an alias
import random as rd # Rename the module to make it easier to refernece in the code

#Importing specific functions:
from random import shuffle # Can import only the specific functions I need from a module

#Importing multiple functions from a module: 
from random import shuffle, randint # Can import multiple functions by separating them with commas.

