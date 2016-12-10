# show a list of all global variables
globals()

# show a list of all local variables
locals()

# use nonlocal to denote a variable that is available in an outer function for example nonlocal v = 2
# use global to denote a variable that is available in the global namespace for example global v = 2

# python uses elif to denote "else if"

# a function max_of_three which returns the maximum number out of 3 numbers a,b,c


def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(max_of_three(1, 2, 3))
print(max_of_three(3, 2, 1))
print(max_of_three(2, 3, 1))

# function is_leap_year(year) - return True or False
# leap year if the remainder of year divided by 400 is 0
# not leap year if the remainder of year divided by 100 is 0
# leap year if the remainder of year divided by 4 is 0
# otherwise not a leap year


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))

# while loop that sums the squares of odd numbers from 1 to 20

x = 1
sum_squares = 0
while x <= 20:
    if x % 2 == 1:
        sum_squares += x * x
        print('Current sum of squares is %d' % sum_squares)
    x += 1

# from years 1985 to 2016, prints a list of leap years

year = 1985
while year <= 2016:
    if is_leap_year(year):
        print (year,"is a leap year")
    year += 1

# named parameter example
# sum_of_three(a_p = a, b_p = a, c_p = a)
# more info at:
# http://www.diveintopython.net/power_of_introspection/optional_arguments.html


# example of range usage
# more info at http://pythoncentral.io/pythons-range-function-explained/
my_range = range(0,9)
len(my_range)
my_iter = iter(my_range)
next(my_iter)
# do something exactly 10 times
for ix in range (0,10):
    print(ix)

# more fun with range
z=10
z in range (-1,5)

# calculate the sum of square roots of all numbers from 2000 to 3200
# only do this for all integers divisible by 5, but not divisible by 7
import math
total = 0
for y in range(2000,3201):
    if y%5 == 0 and y%7 != 0:
        total += math.sqrt(y)
        print("adding", y)
print(total)

# same as above, but using the 3rd parameter for range, which indicates the increment value
total2 = 0
for y2 in range(2000,3201,5):
    if y2%7 != 0:
        total2 += math.sqrt(y2)
        print("adding", y2)
print(total2)

# same as above, but using a while statement
y3 = 2000
total3 = 0
while y3 <= 3200:
    if y3 % 5 == 0 and y3 % 7 != 0:
        total3 += math.sqrt(y3)
    y3+=1
print(total3)

# write a function which will return a sum every 5th number from two parameters start to end
def sum_every_fifth(start, end):
    tot = 0
    for x in range(start, end + 1, 5):
        #print(x)
        tot += x
    return tot

print(sum_every_fifth(0,10))
