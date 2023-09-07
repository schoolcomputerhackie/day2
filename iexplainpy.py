# so basically python is a very easy language
# it is object oriented, meaning it deals with objects
# there are multiple types of variables / objects in python
# the most common ones are strings, integers, floats, and booleans
"this is a string", 'this is also a string' # it is the most common method of storing text / messages
9001 # this is an integer, it is used for storign numbers.
9000.1 # this is a float, it is used for storing decimals, however python does not need to convert to float,
# it does it for you
True, False # these are boolean values, they are used for storing true or false values
# there are also lists, tuples, and dictionaries, but we will get to those later
# now that we know what variables are, we can start to use them
# in python you do not need to specify the type of variable you are using
# you can just say the variable name and set it equal to something
x = 5 # this is an integer
y = 5.0 # this is a float
z = "hello" # this is a string
# if I would want to convert an integer to a string, I would do this
x = str(x) # this converts x to a string
# if i wanted to convert a str to an int, I would do this
z = int(z) # this converts z to an int

# now that we know how to use variables, we can start to use them in functions
# functions are a way to store code that you can use later

# this is a function
def my_function():
    print("hello world")

# to define functions you use "def", your functionm name, parentheses, and a colon
# the colon is essentially a "then", or a "do this"
# if you want to make parameters you can do this

def my_function(x, y):
    print(x + y)

# for example
my_function(5, 5) # this will print 10

# if i wanted to use a string, I would do this
my_function("hello", "world") # this will print "helloworld"

# i cannot use two types though, this will return an error
my_function(5, "hello") # this will return an error

# to mitigate this, I would have to convert the int to a string
my_function(str(5), "hello") # this will print "5hello"

print("hello, world")
#hello, world
# this is a print statement, it is used to print things to the console

if True:
    print("hello, world")
else:   
    print("goodbye, world")

if x == False:
    print("hello, world")
elif x == True:
    print("goodbye, world")

# loops
# there are two types of loops, for loops and while loops
u = True
while True:
    print("hello, world")

# list
# lists are a way to store multiple values in one variable
x = [1, 2, 3, 4, 5]
x[0]

# dict
p = {
    "key": "value",
    "value": 9
}

print(p["value"]) # this will print 9

import random
