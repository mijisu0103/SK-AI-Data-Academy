"""Tuple
A list is a mutable object, whereas a tuple is an immutable object.
Mutable objects allow modifications such as element updates, deletions, and changes. However, immutable objects do not allow such modifications."""

# Creating a Tuple
ex = (1, 2)  # Using parentheses
ex = 1, 2    # Parentheses can be omitted

# Creating a Tuple with a Single Element
ex = (9,)    # Single-element tuple
ex = (9)     # This is not a tuple but an integer
# Always remember to include a comma , when creating a tuple with one element.

"""Tuple Unpacking
You can assign values from a tuple to multiple variables at once:"""
one, two, three = 1, 2, 3

"""Exercise 1:

1. Create mytuple1 using () with the values 1, 2, 3.
2. Create mytuple2 using commas with the values 1, 2, 3.
3. Unpack mytuple2 into variables a, b, and c."""

mytuple1 = (1, 2, 3)
print(mytuple1)

mytuple2 = (1, 2, 3,)
print(mytuple2)

a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

"""Using Tuples
Tuples do not allow modification, deletion, or changes to their elements."""

# Accessing Tuple Elements
ex_tuple = (4, 5)
print(ex_tuple[1])  # Accessing the second element
# To find the size of a tuple, have to use the len() function.

# Converting Between Tuple and List
ex_tuple = (4, 5)
print(list(ex_tuple))  # Convert tuple to list

ex_list = [1, 2, 3]
print(tuple(ex_list))  # Convert list to tuple
# Cannot modify tuple elements, BUT can convert a tuple to a list, modify the list, and then convert it back to a tuple.

"""Exercise 2:

1. Store the element at index 1 of mytuple in the variable a.
2. Store the size of mytuple in the variable b.
3. Convert the list c to a tuple and store it in the variable d.
4. Convert the tuple e to a list and store it in the variable f."""

mytuple = (1, 2, 3)
print(mytuple)

# Indexing
a = mytuple[1]
print(a)

# Tuple size
b = len(mytuple)
print(b)

# List to tuple
c = [1, 2, 3, 4]
d = tuple(c)
print(d)

# Tuple to list
e = (1, 2, 3, 4)
f = list(e)
print(f)

# Modify the list and convert it back to a tuple
f.append(5)
f.remove(2)
g = tuple(f)
print(g)

"""Mission 1:

1. Change the given tuple a to have the values (1, 100, 2, 3, 4)."""

a = (1, 2, 3, 4)
b = list(a)
b.insert(1, 100)
c = tuple(b)
print(c)

"""Set
A set is an unordered collection of unique elements. Duplicate elements are automatically removed."""

"""Exercise 3:

1. Create an empty set myset1.
2. Create a set myset2 with the values 1, 1, 1, 2, 2, 2, 3, 3, 3 (duplicates will be removed).
3. Add the values 1, 2, 3 multiple times to myset2 and observe that duplicates are not allowed."""

myset1 = set()
print(myset1)

myset2 = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(myset2)

myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2)

"""Set Operations
Intersection (& or intersection())
Union (| or union())
Difference (-)"""

"""Exercise 4:

1. Use & or intersection() to print the intersection of sets a and b.
2. Use | or union() to print the union of sets a and b.
3. Print the difference between sets a - b and b - a."""

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a & b)
print(a.intersection(b))

print(a | b)
print(a.union(b))

print(a - b)
print(b - a)

"""Mission 2:

1. Add the number 6 to sample1.

Output:
{1, 2, 3, 4, 5, 6}

2. Remove the number 2 from sample2.

Output:
{4, 5, 6, 7}

3. Print the intersection of sample1 and sample2.
4. Print the union of sample1 and sample2.
5. Print the difference between sample1 and sample2."""

sample1 = {1, 2, 3, 4, 5}
sample2 = {2, 4, 5, 6, 7}

# Add 6 to sample1
sample1.add(6)
print(sample1)

# Remove 2 from sample2
sample2.remove(2)
print(sample2)

# Print intersection
print(sample1 & sample2)

# Print union
print(sample1 | sample2)

# Print difference
print(sample1 - sample2)

"""Dictionary
A dictionary is a collection of key-value pairs."""

"""Exercise 5:

1. Create an empty dictionary mydict1.
2. Create a dictionary mydict2 with the values { 'a': 1, 'b': 2, 'c': 3 }.
3. Create a dictionary mydict3 with keys and values including a mix of types.
4. Store the value of key 'a' from mydict3 in the variable a."""

mydict1 = dict()
print(mydict1)

mydict2 = {'a': 1, 'b': 2, 'c': 3}
print(mydict2)

mydict3 = {'a': 1, '가': 2, 100: 3, 3.14: 4, True: 5}
print(mydict3)

a = mydict3['a']
print(a)

"""Exercise 6:

1. Print all the keys of mydict.
2. Convert the keys of mydict to a list and print it.
3. Print all the values of mydict.
4. Print all the key-value pairs of mydict as tuples."""

mydict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
print(mydict)

print(mydict.keys())
print(list(mydict.keys()))

print(mydict.values())

print(mydict.items())
print(list(mydict.items()))

"""Exercise 7:

1. Add all the key-value pairs from fruit to mydict1.
2. Change the value of key 'a' in mydict2 to 900.
3. Remove the key 'a' from mydict3 and print the value of key 'b'."""

mydict1 = {'Pineapple': 1500, 'Mango': 3500, 'Pear': 1000}
fruit = {'Apple': 2000, 'Strawberry': 3000, 'Watermelon': 5000}
mydict1.update(fruit)
print(mydict1)

mydict2 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
mydict2['a'] = 900
print(mydict2)

mydict3 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
mydict3.pop('a')
print(mydict3['b'])
print(len(mydict3))

"""Mission 3:

1. Create the dictionary score with the following key-value pairs: 'Hajun': 90, 'Seoyun': 86, 'Jia': 80.
2. Add 'Suji': 95 to score.
3. Remove 'Jia' from score.
4. Add the following key-value pairs to score using update(): 'Gichang': 98, 'Namcheol': 60, 'Giseong': 75."""

score = {'Hajun': 90, 'Seoyun': 86, 'Jia': 80}
print(score)

score['Suji'] = 95
print(score)

score.pop('Jia')
print(score)

score.update({'Gichang': 98, 'Namcheol': 60, 'Giseong': 75})
print(score)

