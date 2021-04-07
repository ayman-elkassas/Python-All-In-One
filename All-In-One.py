# todo:variable and strings
# print("Hello world")
# with var
msg = "hello world"
# print(msg)

# todo:concatenation
first_name = "ahmed"
last_name = "mohamed"
# print(first_name + '' + last_name)

# todo:list
bikes = ['trek', 'readline', 'giant']
# get first item
first_item = bikes[0]

# get last item
last_item = bikes[-1]

# looping through list
for bike in bikes:
    print(bike)

# Adding items to a list
bikeList = []
bikes.append('trek')
bikes.append('readline')
bikes.append('giant')
# print(bikes)

# Making numerical lists
squares = []
for i in range(1, 11):
    # ** is square
    squares.append(i ** 2)

# List comprehensions
# [operation then-> loop_def]
squares_com = [
    (x ** 2)
    for x in range(1, 11)
]
# print(squares_com)

# Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
fisrt_two = finishers[:2]
# print(fisrt_two)

# Copying a list
copy_of_bikes = bikes[:]
print(copy_of_bikes)

# todo:Tuple
dimensions = (1920, 1080)

# todo:if statements
# conditional test
# ==,!=,>=,>

# conditional test with lists
# 'trek' in bikes
# 'trek' not in bikes
age = 3
if age > 5:
    trick = 0
else:
    trick = 5

# todo:dictionary
alien = {'color': 'green', 'points': 5}
# Accessing a value
print("The alien's color is " + alien['color'])
# Adding a new key-value pair
alien['x_position'] = 0

# most import literate
# list, dictionary, tuple

# todo:looping
fav_numbers = {'eric': 17, 'ever': 4}
for key, val in fav_numbers.items():
    print(key + 'loves' + str(val))

for key in fav_numbers.keys():
    print(key)

for value in fav_numbers.values():
    print(value)

# Prompting for a value
name = input("What's your name? ")
print("Hello, " + name + "!")

age = input("How old are you? ")
age = int(age)

pi = input("What's the value of pi? ")
pi = float(pi)

# while looping
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

msg = ''
while msg != 'quit':
    msg = input("What's your message? ")
    print(msg)


# todo:simple function
def greet_user():
    """Display a simple greeting."""
    print("hello!")

greet_user()

def greet_user(username):
    """Display a personalized greeting."""
    print("Hello, " + username + "!")

greet_user('jesse')

def make_pizza(topping='bacon'):
    """Make a single-topping pizza."""
    print("Have a " + topping + " pizza!")

make_pizza()
make_pizza('pepperoni')

def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y


sum = add_numbers(3, 5)
print(sum)


# todo:classes
class Dog():
    """Represent a dog"""

    def __init__(self, name=any("sd")):
        """Initialize dog object"""
        self.name = name

    def sit(self):
        """simulating sitting"""
        print(self.name + "is sitting.")


my_dog = Dog('Peso')
print(my_dog.name + "is a greet dog!")
my_dog.sit()

# todo:inheritance
class SARDog(Dog):
    def __init__(self, name):
        # calling initiate method inside parent class
        super().__init__(name)

    def search(self):
        print(self.name)


smallDog = SARDog('willie')
print(smallDog.name)
smallDog.sit()
smallDog.search()

# working with files

# Reading File
filename = 'siddhartha.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

# Writing File
filename = 'journal.txt'
with open(filename,'w') as file_object:
    file_object.write("I love python")

filename = 'journal.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games.")

prompt = "How many tickets do you need? "
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")

# todo:list
users = ['val', 'bob', 'mia', 'ron', 'ned']
# last element
newest_user = users[-1]

users[0] = 'valerie'
users[-2] = 'ronald'

# add element at end of list
users.append('amy')

# Starting with an empty list
users = []
users.append('val')
users.append('bob')
users.append('mia')

# add in specific index
users.insert(0,"aaa")

# remove ele of index
del users[-1]

# remove by val
users.remove("aaa")

# pop element
most_recent_user = users.pop()
print(most_recent_user)

# pop first item
first_user = users.pop(0)
print(first_user)

# length of list
num_users = len(users)
print("We have " + str(num_users) + " users.")

# sorting
users.sort()
# Sorting a list permanently in reverse alphabetical
users.sort(reverse=True)

# Reversing the order of a list
users.reverse()

# print all items in list
for user in users:
    print(user)


# python module
from product import productOfNum
productOfNum.person['name']

# range
for num in range(5): # 0-4
    print(num)

# range(5,10) # 5-9
# numbers = list(range(1, 1000001))

#min,max
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)

#sum
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)

#slicing
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]

# middle three items
middle_three = finishers[1:4]
last_three = finishers[-3:]

#copy
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]

squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)

squares = [x**2 for x in range(1, 11)]

make_upper=[name.upper() for name in finishers]

# tuple
# Getting the value associated with a key
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# Getting the value with get()
alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points',0)
print(alien_color)
print(alien_points)

alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

# Show each person's favorite language,
# in order by the person's name.
for name in sorted(alien_0.keys()):
    print(name + ": ")

# Define a list of users, where each user
# is represented by a dictionary.
users = [
    {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi',
    },
    {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
    },
]
# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")

from collections import OrderedDict
# Store each person's languages, keeping
# track of who respoded first.
fav_languages = OrderedDict()
fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']
# Display the results, in the same order they
# were entered.
for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)

# P7
