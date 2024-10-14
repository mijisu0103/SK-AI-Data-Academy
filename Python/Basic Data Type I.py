# Exercise 1: Print "It's a great day to learn Python today!" using print().

print("It's a great day to learn Python today!")

"""Exercise 2:

1. Set the variable names to lowercase a, uppercase A, and a Korean letter.
2. Set the variable name by combining lowercase a and the number 1.
3. Set the variable name by combining lowercase a and an underscore _.
4. Set the variable name by combining an underscore _ and lowercase a.
5. Uncomment invalid variable names, check the errors, and re-comment to avoid errors."""

a = 1
A = 1
variable = 1

# Valid combinations
a1 = 1
a_ = 1
_a = 1

# Invalid combinations (uncomment to check errors)
# 1a = 1
# * = 7
# a$ = 6
# a b = 6

# Common variable conventions:
test = 10
test01 = 20
test_01 = 30

"""Exercise 3:

1. Use the appropriate function to check the data type.
2. Store an arbitrary integer value in variable d.
3. Store an arbitrary float value in variable e."""

# Check data types
a = type(1)
print(a)

b = type(3.14)
print(b)

c = type("Hello")
print(c)

# Store an integer in `d`
d = 1
print(d)
print(type(d))

# Store a float in `e`
e = 3.14
print(e)
print(type(e))

"""Exercise 4:

1. Store the string "Hello" using single quotes in variable word1.
2. Store the string "Hello" using double quotes in variable word2.
3. Store False in variable a.
4. Store None in variable b."""

word1 = 'Hello'
print(word1)
print(type(word1))

word2 = "Hello"
print(word2)
print(type(word2))

a = False
print(a)
print(type(a))

b = None
print(b)
print(type(b))

"""Exercise 5:

1. Convert the integer variable a to a float and print it.
2. Convert the float variable b to an integer and print it.
3. Convert the boolean variables c and d to integers and print them.
4. Convert the boolean value True to a float and print it."""

# Convert int to float
a = 1
print(type(a))
print(float(a))

# Convert float to int
b = 3.99
print(int(b))

# Convert boolean to int
c = True
print(int(c))

d = False
print(int(d))

# Convert boolean `True` to float
print(float(True))

""" Mission 1:

1. Check the type of variable a.
2. Change the type of variable b.
3. Change the type of variable c.
4. Change the type of variable d.
5. Change the type of variable e."""

a = 3.14
print(type(a))

b = 1
print(float(b))

c = 1
print(bool(c))

d = False
print(int(d))

e = 123
print(str(e))

"""Exercise 6:

1. Create an empty list using [] and store it in mylist1.
2. Create an empty list using list() and store it in mylist2.
3. Create a list with the values [1, 3, 2, 4, 5] and store it in mylist3."""

mylist1 = []
print(mylist1)

mylist2 = list()
print(mylist2)

mylist3 = [1, 3, 2, 4, 5]
print(mylist3)

"""Exercise 7:

1. Store the list [1, 2, 3] in variable a.
2. Store the list [1, 'hello', 3, 3.14, True] in variable b.
3. Store the list [1, 'hello', 3, 3.14, [6, 7, '8']] in variable c."""

a = [1, 2, 3]
print(a)

b = [1, 'hello', 3, 3.14, True]
print(b)

c = [1, 'hello', 3, 3.14, [6, 7, '8']]
print(c)

"""Exercise 8:

1. Add the number 1 to the end of the list mylist.
2. Add three 7s, one 3, one 5, and one 2 to the end of the list mylist.
3. Insert 100 at index 1 in mylist."""

mylist = []
print(mylist)

mylist.append(1)
print(mylist)

mylist.append(7)
mylist.append(7)
mylist.append(7)
mylist.append(3)
mylist.append(5)
mylist.append(2)
print(mylist)

mylist.insert(1, 100)
print(mylist)

"""Exercise 9:

1. Remove the first occurrence of the number 7 from mylist.
2. Remove and return the element at index 1 from mylist.
3. Print the number of elements in mylist."""

mylist = [1, 100, 7, 7, 7, 3, 5, 2]

mylist.remove(7)
print(mylist)

mylist.pop(1)
print(mylist)

print(len(mylist))

"""Exercise 10:

1. Sort mylist1 in ascending order and print it.
2. Sort mylist2 in descending order and print it.
3. Extend the list a with [4, 5] and print it."""

mylist1 = [1, 6, 3, 2, 7, 5, 4]
mylist1.sort()
print(mylist1)

mylist2 = [1, 6, 3, 2, 7, 5, 4]
mylist2.sort(reverse=True)
print(mylist2)

a = [1, 2, 3]
a.extend([4, 5])
print(a)

"""Mission 2:

1. Add "X-Men" to the end of the list movie and print it.
2. Insert "Deadpool" at index 1 in movie and print it.
3. Remove "Iron Man" from the list movie and print it.
4. Remove the element at index 1 in movie and print the result.
5. Extend movie by adding the list kr_movie and print it.
6. Sort movie alphabetically and print it."""

movie = ['Avengers', 'Iron Man', 'Thor', 'Spider-Man']

# Add 'X-Men'
movie.append('X-Men')
print(movie)

# Insert 'Deadpool' at index 1
movie.insert(1, 'Deadpool')
print(movie)

# Remove 'Iron Man'
movie.remove('Iron Man')
print(movie)

# Remove element at index 1
movie.pop(1)
print(movie)

# Extend with Korean movies
kr_movie = ['Space Sweepers', 'New World', 'Tazza']
movie.extend(kr_movie)
print(movie)

# Sort alphabetically
movie.sort()
print(movie)

"""Exercise 11:

1. Use indexing to print the first element ('P') in mylist.
2. Use indexing to print the fourth element ('H') in mylist.
3. Use negative indexing to print the first element ('P') in mylist.
4. Use negative indexing to print the fourth element ('H') in mylist."""

mylist = ['P', 'Y', 'T', 'H', 'O', 'N']

# Print first element
print(mylist[0])

# Print fourth element
print(mylist[3])

# Negative indexing for first element
print(mylist[-6])

# Negative indexing for fourth element
print(mylist[-3])

"""Exercise 12:

1. Use index access to change the first value in mylist to 999.
2. Use reverse index access to change the second value in mylist to 300."""

mylist = [10, 20, 30, 40, 50]

# Change the first element to 999
mylist[0] = 999
print(mylist)

# Change the second element from the end to 300
mylist[-4] = 300
print(mylist)

"""Exercise 13:

1. Use nested indexing to print the element at index 1,1 of mylist.
2. Change the value at index 1,1 to 99 and print the updated mylist."""

mylist = [['a', 'b', 'c'], [4, 5, 6], 7, 8, 9]

# Print the list at index 1
print(mylist[1])

# Print the element at index 1,1
print(mylist[1][1])

# Change the element at index 1,1 to 99
mylist[1][1] = 99
print(mylist)

"""Exercise 14:

1. Use [:] to print the entire list mylist.
2. Use [start:] to print mylist from index 2 to the end.
3. Use [:end] to print mylist up to index 3.
4. Use [start:end] to print mylist from index 1 to 3."""

mylist = [100, 200, 300, 400, 500]

# Print the entire list
print(mylist[:])

# Print from index 2 to the end
print(mylist[2:])

# Print from the start to index 3
print(mylist[:3])

# Print from index 1 to 3
print(mylist[1:3])

"""Mission 3:

1. Use list indexing & slicing to print the following result: ['Pineapple', 'Pear', 'Watermelon'].
2. Use list indexing & slicing to print the following result: ['Mango', 'Strawberry'].
3. Use list indexing & slicing to print the following result: ['Apple', 'Banana', 'Pineapple'].
4. Use list indexing & slicing to print the following result: ['Pear', 'Watermelon', 'Kiwi', 'Orange', 'Mango', 'Strawberry']."""

fruit = ['Apple', 'Banana', 'Pineapple', 'Pear', 'Watermelon', 'Kiwi', 'Orange', 'Mango', 'Strawberry']

# Slicing: Pineapple to Watermelon
print(fruit[2:5])

# Slicing: Mango and Strawberry
print(fruit[-2:])

# Slicing: Apple to Pineapple
print(fruit[0:3])

# Slicing: Pear to Strawberry
print(fruit[3:])

"""Exercise 15:

1. Use indexing and step to print every second element of mylist.
2. Use indexing and step to print mylist in reverse.
3. Use indexing and step to print mylist in reverse, skipping every two elements."""

mylist = [100, 200, 300, 400, 500]

# Print every second element
print(mylist[::2])

# Print list in reverse order
print(mylist[::-1])

# Print list in reverse, skipping every two
print(mylist[::-2])

"""Mission 4:

1. Use slicing to print only the even numbers from the nums list.
2. Use slicing to reverse the sample list and print it.
3. Use slicing to print [3, 5, 7] from the sample list.
4. Use slicing to print [2, 5, 8] from the sample list.
5. Create a nested list myList and print it.
6. Add 9 to the third sublist in myList and print the updated list."""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print only even numbers
print(nums[1::2])

sample = [1, 2, 3, 4, 5, 6, 7, 8]

# Reverse the list
print(sample[::-1])

# Print [3, 5, 7]
print(sample[2:7:2])

# Print [2, 5, 8]
print(sample[1::3])

# Create a nested list
myList = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(myList)

# Add 9 to the third sublist
myList[2].append(9)
print(myList)



