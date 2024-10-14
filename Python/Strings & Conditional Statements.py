"""Exercise 1:

1. Store the following string in a using single quotes ('):
Hello, nice to meet you.

2. Store the following string in b using double quotes ("):
Hello, nice to meet you.

3. Store the following multiline string in sample:
Hello?
Nice to meet you.
My name is
Python."""

a = 'Hello, nice to meet you.'
print(a)

b = "Hello, nice to meet you."
print(b)

sample = """Hello?

Nice to meet you.

My name is

Python."""
print(sample)

"""Exercise 2:

Try printing various types of strings."""

print('Hello Python')

print('First string', 'And, second string')

# Using % for formatting
print("Hello? %s" % ('Nice to meet you.'))
print('Hello? %.4f' % (0.123456))
print('Hello? %d' % (12345))
print('Hello? %c' % ('a'))

# Using {} with .format()
print('Welcome to? {}'.format('Python.'))
print('Password {}'.format(486))
print('Pi? {:.2f}'.format(3.141592))  # Rounds to two decimal places

# f-string formatting (Python 3.6+)
name = 'Pengsoo'
age = 10
print(f'My name is {name}. I am {age} years old.')
print(f'I will be {age + 1} next year.')
d = {'name': 'Pengsoo', 'age': 10}
print(f"Nice to meet you. I'm {d['name']}. I am {d['age']} years old.")

"""Mission 1:

1. Use variable a to format and print:
The value of a is 1234.

2. Use variables a and b to format and print the following. Round the values to three decimal places:
The value of a is 3.142, the value of b is 6.181"""

a = 1234
print("The value of a is %d." % (a))

a = 3.141592
b = 6.181112
print(f'The value of a is {a:.3f}, the value of b is {b:.3f}.')

"""Exercise 3:

String slicing:

[start:stop:step]: Extracts a portion of the string.
[:]: Extracts the whole string.
[start:]: From the start index to the end.
[:end]: From the beginning up to the end index (exclusive).
[::-1]: Reverses the string.

Instructions:

1. Store the lengths of the following strings in b, c, d, and e:
'banana'
'banana pen'
'한글'
'한글 킹왕짱'

2. Store index 0 and -2 of string a in f and g.

3. Use string slicing to:
  Store from index 3 to the end in i.
  Store from index -4 to the end in j.
  Store from the start to index 6 in k.
  Store from the start to index -3 in l.
  Store from index 3 to index 6 in n.
  Store every second character in m.
  Reverse the string in o."""

b = len('banana')
c = len('banana pen')
d = len('한글')
e = len('한글 킹왕짱')

print(b, c, d, e)

a = 'Python is my life'
f = a[0]
g = a[-2]

print(f, g)

i = a[3:]
j = a[-4:]
k = a[:6]
l = a[:-3]
n = a[3:6]
m = a[::2]
o = a[::-1]

print(i, j, k, l, n, m, o)

""" Mission 2:

1. Slice the string sample to extract the date and weather:
date: 20210101, weather: Sunny

2. Extract the last four digits of the following license plate number:
license_plate = "13나 5645" """

sample = '20210101Sunny'
date = sample[:-5]
weather = sample[-5:]
print(f'date: {date}, weather: {weather}')

license_plate = "13나 5645"
print(license_plate[-4:])

"""Exercise 4:

1. Concatenate variables a and b.
2. Repeat a twice.
3. Repeat the string 'abc' five times.
4. Repeat the string '===' seven times."""

a = 'Hello!'
b = 'Welcome to Python'

print(a + b)
print(a * 2)
print('abc' * 5)
print('===' * 7)

"""Exercise 5:

1. Split a by spaces and store in d.
2. Split b by hyphens and store in e.
3. Split c by spaces and store in f."""

a = 'This is a pen'
d = a.split(' ')
print(d)

b = 'This-is-a-pen'
e = b.split('-')
print(e)

c = '한글은 어떻게 될까요?'
f = c.split(' ')
print(f)

""" Mission 3:

1. Split the string sample into two parts:
['abc-def', '789/100']

2. Split sample differently:
['abc', 'def.789/100']"""

sample = 'abc-def.789/100'
print(sample.split('.'))
print(sample.split('-'))

""" Exercise 6:

1. Join elements of a with hyphens.
2. Join characters of b with hyphens."""

a = ['010', '1234', '5678']
print('-'.join(a))

b = 'ABCDE'
print('-'.join(b))

""" Mission 4:

1. Join elements of sample with *:
Python*is*too*interesting

2. Join elements of phone_number with -:
010-1234-5678"""

sample = ['Python', 'is', 'too', 'interesting']
print('*'.join(sample))

phone_number = ['010', '1234', '5678']
print('-'.join(phone_number))

"""Exercise 7:

1. Convert a to lowercase and print it.
2. Convert a to uppercase and print it.
3. Replace .png with .jpg in c and print the result.
4. Remove the leading and trailing spaces in d and print the result."""

a = 'My name is Teddy'
print(a.lower())
print(a.upper())

b = '한글에는 대소문자가 없어요ㅠ'
print(b.lower())
print(b.upper())

c = '01-sample.png'
print(c.replace('.png', '.jpg'))

d = '    01-sample.png                '
print(d.strip())

"""Exercise 8:

1. Add variables a and b.
2. Add 5 to c and assign the result back to c.
3. Subtract e from d.
4. Subtract 3 from f and assign the result back to f.
5. Divide g by h.
6. Divide i by 2 and assign the result back to i.
7. Multiply j and k.
8. Multiply l by 3 and assign the result back to l."""

a = 10
b = 3
print(a + b)

c = 10
c += 5
print(c)

d = 10
e = 3
print(d - e)

f = 9
f -= 3
print(f)

g = 10
h = 3
print(g / h)

i = 10
i /= 2
print(i)

j = 10
k = 3
print(j * k)

l = 20
l *= 3
print(l)

"""Exercise 9:

1. Find the integer quotient when dividing a by b.
2. Find the remainder when dividing a by b.
3. Compute a raised to the power of b.
4. Ensure that 10 + 2 is calculated first using parentheses."""

a = 10
b = 3

print(a // b)
print(a % b)
print(a ** b)
print((10 + 2) * 5)

# What happens here?
c = '10'
d = '20'
print(c + d)  # Concatenation of strings

# Uncomment the next lines to observe the error:
# e = '10'
# f = 20
# print(e + f)  # Error: You cannot concatenate strings and integers

""" Mission 5:

1. Add a and b to print the following result. Do not modify the values of a and b:
30

2. Add a and b to print the following result (as a string):
1020"""

a = '10'
b = 20

# Mission 5.1
print(int(a) + b)

# Mission 5.2
print(a + str(b))

""" Exercise 10:

1. Store the result of 1 > 2 in a.
2. Store the result of 10 >= 10 in b.
3. Store the result of 9 < 10 in c.
4. Store the result of 8 <= 7 in d.
5. Store the result of 2 == 2 in e.
6. Store the result of 2 == 3 in f.
7. Store the result of 2 != 2 in g.
8. Store the result of 1 != 2 in h."""

a = 1 > 2
print(a)

b = 10 >= 10
print(b)

c = 9 < 10
print(c)

d = 8 <= 7
print(d)

e = 2 == 2
print(e)

f = 2 == 3
print(f)

g = 2 != 2
print(g)

h = 1 != 2
print(h)

""" Exercise 11:

1. Write an if statement to print "True" when 5 > 3.
2. Write an if-else statement to print either:
  'if block executed' when 5 < 3, or
  'else block executed' otherwise.
3. Add an elif block to print "elif block" when 3 < 4."""

# 5 > 3 is True, so it prints "True"
if 5 > 3:
    print('True')

# else block executes because 5 < 3 is False
if 5 < 3:
    print('if block executed')
else:
    print('else block executed')

# Adding an elif block
if 3 > 5:
    print('if block')
elif 3 < 4:
    print('elif block')
else:
    print('Neither if nor elif')

""" Mission 7:

1. Write a program that accepts a score as input and prints:
  A for scores 90 and above.
  B for scores 80 and above.
  C for scores 70 and above.
  D for scores below 70.
2. Print "Error" for scores less than 0 or greater than 100. """

print('Enter your score: ')
score = int(input())

if score < 0 or score > 100:
    print('Error')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('D')

"""Exercise 12:

1. Use a ternary operator to print "30 years or older" if age1 is 30 or above, otherwise "Under 30".
2. Use a ternary operator to print "30 years or older" if age2 is 30 or above, otherwise "Under 30"."""

age1 = 35
age2 = 20

print("30 years or older" if age1 >= 30 else "Under 30")
print("30 years or older" if age2 >= 30 else "Under 30")

"""Mission 6:
1. Use a ternary operator to print:
  "You are overweight" if the weight is over 100 kg.
  "You have a normal weight" if it is 100 kg or less."""

print('Enter your weight: ')
weight = int(input())

print('You are overweight' if weight > 100 else 'You have a normal weight')

"""Exercise 13:

1. Complete the following tasks using logical operators (and, or, not):"""

# and operator
if (0 < 1) and (0 < 2):
    print('Both A and B are true')
else:
    print('False')

if (0 < 1) and (0 > 2):
    print('Both A and B are true')
else:
    print('False')

# or operator
if (0 < 1) or (1 < 0):
    print('At least one of A or B is true')
else:
    print('False')

if (10 < 1) or (1 < 0):
    print('At least one of A or B is true')
else:
    print('False')

# not operator
if not True:
    print('This will not print')

if not False:
    print('This will print')

