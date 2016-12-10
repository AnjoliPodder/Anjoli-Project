'''
example of how to set default values in a function - this then becomes an optional parameter
in the example below, if you give the function one parameter, it multiplies by the default (2)
if given two parameters, it multiples the values together
'''

def mult(a, b = 2):
    return a * b

print(mult(5,7))  #answer is 35
print(mult(5))  #answer is 10, because the second paramter is not provided, and we use the default of 2

'''
Error handling - more examples in err_handling.py in the pyintro_stu project
'''

a = 1
b = 0  # try changing 0 to another number and see what happens

try:
    c = 1 / b  # do some stuff
    print("The result is", c)  # step to do if there is no exception in the line above
except Exception as ex:
    print("Something bad happened")  # what to do if an exception is caught
    print(type(ex), ":", ex)
finally:
    print("My function has ended") # code to execute always, regardless of whether exception occurred or not

# Throwing your own exceptions
'''
import math
my_var = math.exp(math.pi*10)
if my_var > 10E4:
    raise ArithmeticError('Too large %.2f' % my_var)
'''

'''
CLASS FUNCTIONS
some examples of Class functions - isinstance, type
'''

class Animal: pass
class Dog(Animal): pass
class Whale(Animal): pass

fluffy = Dog()
moby = Whale()
isinstance(moby, Animal)
isinstance(fluffy, Animal)
isinstance(fluffy, Dog)
isinstance(fluffy, Whale)
type(moby)
type(fluffy)
type(100)
type(1.1)
type(moby) == type(fluffy)
type(moby) == type(Whale())

# given a variable x - check if it is of type int
# type(x) == type(int())

# Class exercise: write a function which will determine the type of x which is given as a parameter to
# the function type_checker
#
# returns the type of x as a string (int, float or string)
# if x is a different type, raise a TypeError exception "Unknown Type"

def type_checker(x):
    if type(x) == type(int()):
        return 'int'
    elif type(x) == type(str()):
        return 'str'
    elif type(x) == type(float()):
        return 'float'
    else:
        raise TypeError("I've encountered an Unknown Type")

# test cases for type_checker function
print(type_checker("hey"))  # check for String
print(type_checker(1))      # check for int
print(type_checker(1.0))    # check for float

# catch the exception
import fractions
try:
    print(type_checker(fractions.Fraction(1, 2)))
except TypeError:
    print("I caught a Type Error Exception")
finally:
    print("I've finished")

'''
RECURSIVE FUNCTIONS
'''
# recursive function example to calculate the nth Fibonacci number

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print (fib(8))

# a more efficient way to calculate Fibonacci sequence - without the function calling itself
def fib2(n):
    if n == 0 or n == 1:
        return n
    fib_n_1 = 0
    fib_n_2 = 1
    for ix in range(2, n + 1):
        fib_result = fib_n_1 + fib_n_2
        fib_n_1 = fib_n_2
        fib_n_2 = fib_result
    return fib_result

print(fib2(8))

# Class exercise: write a recursive function that computes a factorial (factorial of n is 1*2*3*4*...n)
def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(3))

'''
STRINGS
'''
my_str = "This is a string"     # create a string
my_str2 = str(100)              # turn an object of another type (in this case int) to a string
len(my_str)                     # returns the length of the string
my_str += ' and I have added more chars'  # plus operator concatenates two strings
my_str.find("is")               # find the char reference of the substring in the string, returns -1 if not found
my_str.index("is")              # find the index of the substring in the string - but raises an exception if not found
my_str[:10]                     # Return the first 10 chars of the string
my_str[-10:]                    # Return the last 10 chars of the string
my_str[3:10]                    # Return characters 4-10 in the string
my_str.upper()                  # Change to upper case
my_str.lower()                  # Change to lower case
my_str.count("s")               # Count the instances of the substring in the string
my_str.count("s", 30)           # Count the instances of the substring from char 30 onwards
words = my_str.split(' ')       # Create a list of strings, split at every space
"chars" in my_str               # Returns boolean - True if the first string is in the second string
str = "This is a sentence"

for ch in "chars":              # Iterate through the letters in a string
    print(ch)

