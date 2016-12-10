####################### HOME WORK 03 #############
''''''

'''

The purpose of this home work is to practice defining our own functions, using
mathematical modules like math and random, and working with strings. Please read carefully.

==========================  PART 1  ==========================
Implement function histogram(outcomes_freq) which takes a single parameter: a list of integers
The function returns no value. For each integer in the list the function prints a string comprised of
"*" chaaracter (the length of the string is determined by the integer)
Hence, for an input list [1,2,3] the function must print

*
**
***

==========================  PART 2  ===========================
Implement function reverse(in_str, use_loop = False) which by default uses slice operator
to reverse in_str. If use_loop set to true the function does the same using a for loop.
Return a reversed string.

==================================  PART 3 ==================
Write a function called quad_roots() which takes three arguments (parameters): a, b, and c

The function solves a quadratic equation of the form:
a*x^2 + b*x + c = 0
The a, b, and c are constants in this equation

Please see a page on Wikipedia:
https://en.wikipedia.org/wiki/Quadratic_formula

The quad_roots() must compute two roots of the quadratic equation and return them to the
caller. Note that sometimes the roots of a quadratic function are complex numbers. But we know that
Python supports complex numbers and operations with complex numbers. Nevertheless, for simplicity
our function will not proceed with root computation when the roots are complex.

To determine whether the roots are complex, inside the quad_roots() function compute
what is known as "determinant"

determinant = b^2 - 4*a*c

If determinant is a negative number, return from the function immediately with two None values.
Otherwise, proceed with the rest of the root computation and return the two real roots of the equation.

To test your function, please use provided in this file test cases. See the actual code below.
Hint: use math.sqrt() function for implementation

==================================  PART 4 ==================
Write a function rand_color() which returns a random string 'red', 'green' or 'blue'
Implement the function by generating a random integer from the closed interval [0,2], i.e.
any integer 0, 1, or 2. Then use the random integer to return string 'red' if the value of the random integer is 0,
'blue' if the value is 1, or 'green' if the value is 2.

Hint: use random.rand_int() function.
For documentation use https://docs.python.org/2/library/random.html
or execute help(random.randint) in REPL (REPL is the interactive Python console with >>>> prompt).
Do not forget to import the module first!

'''

################ your function definitions go here ###########
# Part 1


def histogram(outcomes_freq):
    for ix in outcomes_freq:
        print('*' * ix)

# Part 2


def reverse(in_str, use_loop=False):
    if use_loop:
        rev_string = ''
        for x in in_str:
            rev_string = x + rev_string
        return rev_string
    else:
        return in_str[::-1]

# Part 3


import math


def quad_roots(a, b, c):
    determinant = b ** 2 - 4 * a * c
    if determinant < 0:
        return None, None
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return x1, x2

# Part 4


import random


def rand_color():
    x = random.randint(0, 2)
    if x == 0:
        return 'red'
    elif x == 1:
        return 'blue'
    else:
        return 'green'


################    PART 1 the test cases          ############


histogram([1, 2, 3, 0, 10, 2, 11, 13, 5])
histogram([12, 1, 6, 8])

################    PART 2 the test cases          ############


print(reverse("This is a test!", use_loop=True))
print(reverse("This is another test!", use_loop=False))

################    PART 3 the test cases          ############


x1, x2 = quad_roots(1, -5, c=9/4)
print('x1 = %s, x2 = %s' % (x1, x2))

x1, x2 = quad_roots(1, -5, 0.)
print('x1 = %s, x2 = %s' % (x1, x2))

x1, x2 = quad_roots(10, -2, 1)
print('x1 = %s, x2 = %s' % (x1, x2))

x1, x2 = quad_roots(4., 10., 1)
print('x1 = %s, x2 = %s' % (x1, x2))

x1, x2 = quad_roots(8., -2., 10.)
print('x1 = %s, x2 = %s' % (x1, x2))

############### PART 4 test cases ##############
print(rand_color())
print(rand_color())
print(rand_color())
print(rand_color())
print(rand_color())