'''
TUPLES
'''

# Useful for efficiency reasons as Python allocates exactly the right amount of meemory (since they are immutable)
# Lists can grow, so more memory is allocated as needed


# example: swap the values of two variables


x = 1
y = 2
x, y = y, x

# assign the value of two variables at once


x, y  = 3, 4

# function that returns two values
def mf():
    a = 500
    b = "a string"
    return a, b

# assign values to a single variable - this will be a tuple


a = mf()
type(a)  # tuple

# assign values to multiple variables. These will take on the types of the returned values


a, b = mf()
type(a) # integer
type(b) # string

# tuple are immutable objects
tp = ()
type(tp)
tp = ("Hey", 1, 3.0, "You")
tp[1]  # returns the element at index 1 (2nd in the list)

# tp[1] = 500  # this won't work as a tuple is immutable

# unpacking a tuple - you can pass multiple values to a function with multiple arguments in a tuple
def dummy(city, address, zip):
    print(city, address, zip)

dummy('New York', '25 Broadway', 1002)

tp = ('New York', '25 Broadway', 1002)
dummy(*tp)  #the * notation tells Python to unpack the tuple into multiple arguments


'''
MAP
'''

# a slow way to square the elements in a list


y = [1, 2, 3, 4]
y_sq = [0]* len(y)
for ix, el in enumerate(y):
    y_sq[ix] = el**2
y_sq

# a faster way using map - no need to use a loop. Goes through each element of the list and runs the function on it


def sq_this(x):
    return x**2
result = list(map(sq_this, y))


# given a list of 4 sentences, split each sentence into a list of words
# use m
# ap to do this

sentences = ["this is a sentence", "another sentence", "The quick brown fox", "Once upon a time"]

# have to define our own version of split


def my_split(sentence):
    return sentence.split(' ')
result2 = list(map(my_split, sentences))

# take a list of temperatures in celsius and return a list of fahrenheit


def convert_temp(temp):
    return temp * 9 / 5 + 32

temperatures = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
converted = list(map(convert_temp, temperatures))


# you can use multiple lists gother with map
# the following example searches for the keyword in the corresponding sentence (e.g first with first, second with second)
# the map stops when one of the lists is exhausted - extra values in keyword list will be ignored

sentences = ["this is a sentence", "another sentence", "The quick brown fox", "Once upon a time"]
keywords = ["sent", "ther", "brow", "whatever", "another", "fox"]

def check_key(astr, key):
    return astr.find(key)

found = list(map(check_key, sentences, keywords))   # returns a list with the position of the keyword in the sentence


# check whether each keyword is in any of the sentences in a list using a map function
# print the first keyword that is found


def find_keywords(k_list, s_list):
    for el in k_list:
        el_list = [el]*len(s_list)
        found = list(map(check_key, s_list, el_list))
        if found != [-1] * len(s_list):  # check against a list of -1 values - -1 means the keyword was not found
            print(el)
            return
    print("No keywords found")

sentences2 = ["this is a sentence", "another sentence", "The quick brown fox", "Once upon a time"]
keywords2 = ["hahaha", "whatever", "sent"]
find_keywords(keywords2, sentences2)


'''
FILTER
'''

# filter the odd numbers from a list of numbers


my_list = range(1, 21)

# helper function - should evaluate to Boolean
# needs to take an argument


def helper(el):
    return not(el % 2 == 0)

# filter will return all results where the helper function evaluated to True


list(filter(helper, my_list))

# you have a list of strings. Filter out those strings that are longer than 10 chars. Leave only the short ones.


def shorter_than(my_string, cutoff=10):
    return len(my_string) < cutoff

string_list = ["hello", "this", "is", "a", "reallylongstring", "anotherlongstring"]
holidays = ["Christmas", "Thanksgiving", "Fourth Of July", "Easter", "Australia Day", "Passover"]
print(list(filter(shorter_than, string_list)))
print(list(filter(shorter_than, holidays)))


'''
LAMBDA FUNCTIONS
'''


f = lambda x:   x**2
type(f)         # f is type function
f(4)            # a way to reference the function and give it an argument


adder = lambda x, y: x + y  # an example with multiple arguments
adder(1, 3)

myfunc = adder
myfunc(2, 4)

adder2 = lambda x, y: (x + y, x - y)
adder2(4, -4)

# write a lambda function that takes two parameters and returns True if the parameters are identical and equal


check = lambda x, y: (x == y) and (x is y)

# use lambda and map in an adder for two lists


list1 = [1,2,3,4]
list2 = [1,2,4,5]

list(map(lambda x, y: x + y, list1, list2))

# take 2 lists of numbers, each list contains one side of a right angled triangle. Compute the length of the 3rd side
# use the pythagoras theorem


side_a = list(range(100,111))
side_b = list(range(50,61))
import math
list(map(lambda a, b: math.sqrt(a**2 + b**2), side_a, side_b))


# filter using a lambda function - go back to the holiday example and return holiday names < 10 chars

holidays = ["Christmas", "Thanksgiving", "Fourth Of July", "Easter", "Australia Day", "Passover"]
list(filter(lambda x: len(x) < 10, holidays))

'''
CLOSURES
'''

# more info in the notes!

def comp(threshold):
    return lambda x: x < threshold


'''
LIST COMPREHENSIONS
'''

comp1 = [x + 1 for x in range(1,10) if x % 2 == 0 ]  # creates a list by adding 1 to every even element in
                                                     # the original list

holidays = ["Christmas", "Thanksgiving", "Fourth Of July", "Easter", "Australia Day", "Passover"]
comp2 = [h for h in holidays if len(h) < 10]  # back to the holidays example - using list comprehension instead
comp3 = [(h, len(h)) for h in holidays]

# example using a nested if statement


comp4 = [ix*ik for ix in range(1,4) for ik in range(1,3)]

ll = [[1,2,3]]*4
ll  # a list of lists
ll[0][0] = 100
ll  # notice that the first element in EVERY list changes to 100 - not just the first one


# using list comprehension, generate a list of integers that are divisible by 7 but not divisible by 3
# in the range 2000 to 3200

comp5 = [n for n in list(range(2000, 3201)) if n % 7 == 0 and n % 3 != 0]


# using list comprehension, take the list of holidays and split each string into individual chars


comp6 = [[ch for ch in hl] for hl in holidays]

# change holidays to uppercase

holidays = ["Christmas", "Thanksgiving", "Fourth Of July", "Easter", "Australia Day", "Passover"]
comp7 = [hl.upper() for hl in holidays]

