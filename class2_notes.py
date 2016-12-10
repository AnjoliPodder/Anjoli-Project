## Python Class 2 ##

def adder(a, b):
    return a + b;
type(adder)

# do nothing
def do_nothing():
    pass;

# a, b and c are three sides of a triangle.
# Check whether this is a right angled triangle (given c is the longest side)
def check_right(a, b, c):
    return(a**2 + b**2 == c**2)

print(check_right(3, 4, 5))

# a function to swap two numbers (immutable example)
def swap(x,y):
    temp = y
    y = x
    x = temp
    return x,y
x=5
y=6
print("The swap of (" + str(x) + ", "+str(y) + ") is " + str(swap(x,y)))

#math module works with float and int
import math
math.sin(math.pi)

#cmath module works with complex numbers
import cmath

## print local scope
print(locals())

## print global scope
print(globals())

#random numbers can be generated with random
import random
random.gauss(0.,1.)

#inner function example
def outer_func():
    def inner_func():
        pass

#passing a variable from the outer to the inner function - use nonlocal
def my_func():
    global x #reference a global variable from within this function
             # you can now make changes to this variable
    x += 5
    temp = 10
    def helper():
        nonlocal temp
        temp += x #you can reference variable x (which was defined outside of the function
                  #however you can't change the value of x
    helper()
    return temp

print(my_func())

# example of a function in the random module
import random
def three_random():
    return(random.randint(1,3)*random.randint(1,3)*random.randint(1,3))

print("the product of three randoms is", three_random())

def three_random2(start,end):
    return(random.randint(start,end)*random.randint(start,end)*random.randint(start,end))

print("the product of three other randoms is", three_random2(1,6))

## exercise to demonstrate inner functions
## function high fever - takes one argument - temp in C
## convert to F and then return true if temp in F is over 101.5

def high_fever(temp_c):
    def convert():
        return temp_c * 9/5 + 32 #we can reference the outer argument in the inner function
    return convert() > 101.5

print(high_fever(39))







