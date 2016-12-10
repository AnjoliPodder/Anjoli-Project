'''
'''

'''
The purpose of this home work is to practice defining our own functions and using
mathematical modules like math and random. Please read carefully.
'''

'''
PART I
Implement a function x_coordinate() which given
initial coordinate x_0, initial speed v_0, acceleration accel calculates
x coordinate of a particle at time t. The analytical formula is:

x = x_0 + v_0*t + 1/2 * accel * t * t
'''

def x_coordinate(x_0, v_0, accel, t):
    x = x_0 + v_0*t + 1/2*accel*t*t
    return x;

'''
test your function with the following inputs
x_0     v_0     accel       t
0       0       1.          1.
1.      0       1.          10.
10.     2.      0.          10.

'''

print("x_coordinate is",x_coordinate(0, 0, 1., 1))
print("x_coordinate is",x_coordinate(1., 0, 1., 10.))
print("x_coordinate is",x_coordinate(10., 2., 0., 10.))


'''
PART II
Note: import math module to solve this problem
Implement a function df() which calculate a discount factor using continuously compounded rate.
The function has two parameters: annual rate and time (in years)
'''

import math
def df(rate, t):
    return math.e**(-rate*t)

# test cases
rate = 0.05
t_to = 2.
print('rate %.2f\tT = % 0.1f\tdf = %.4f' % (rate,  t_to, df(rate, t_to) ) )

rate = 0.05
t_to = 1.
print('rate %.2f\tT = % 0.1f\tdf = %.4f' % (rate,  t_to, df(rate, t_to) ) )

rate = 0.05
t_to = 3.
print('rate %.2f\tT = % 0.1f\tdf = %.4f' % (rate,  t_to, df(rate, t_to) ) )

rate = 0.
t_to = 1.
print('rate %.2f\tT = % 0.1f\tdf = %.4f' % (rate,  t_to, df(rate, t_to) ) )

rate = 0.02
t_to = 5.
print('rate %.2f\tT = % 0.1f\tdf = %.4f' % (rate,  t_to, df(rate, t_to) ) )

rate = 0.02
t_to = 10.
print('rate %.2f\tT = % 0.1f\tdf = %.4f' % (rate,  t_to, df(rate, t_to) ) )


'''
PART III
Note:
Annuities are essentially a series of fixed payments required from you, or paid to you,
at a specified frequency over the course of a fixed time period.
The most common payment frequencies are yearly, semi-annually (twice a year),
quarterly and monthly.

Implement a function pv_annuity() which calculates present value of an annuity and
takes the following arguments:

pmt -  payment per period
rate - interest rate, i.e. discount rate
num_p - number of periods

http://www.financeformulas.net/Present_Value_of_Annuity.html
pv_annuity =  pmt * ( 1 - (1+rate) ** -num_p  ) / rate
'''

def pv_annuity(pmt, rate, num_p):
    return pmt * ( 1 - (1+rate) ** -num_p  ) / rate

pmt =  1000.
rate = 0.05
num_p = 5
print('%.2f' % pv_annuity(pmt, rate, num_p))


pmt =  100.
rate = 0.02
num_p = 10
print('%.2f'  % pv_annuity(pmt, rate, num_p))

'''
PART IV
Implement a function which computes a distance between two randomly selected points on a 2-D plane
Each coordinate could be in range between -100 to 100 inclusively. The range must be passed as parameters
to the function
Hint: use randint() function available in module random. Use sqrt() from module math.
Distance between two points on a 2-D plane is computed as follows
dist = sqrt( (x1 - x2)**2 + (y1 - y2)**2)
where two points have the following coordinates  (x1,y1) and (x2,y2)
'''
import random
def rand_dist(coord_min, coord_max):
    x1 = random.randint(coord_min, coord_max)
    y1 = random.randint(coord_min, coord_max)
    x2 = random.randint(coord_min, coord_max)
    y2 = random.randint(coord_min, coord_max)
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print('############### Random distances #################')
print('%.2f' % rand_dist(-100,100))
print('%.2f' % rand_dist(-10,10))
print('%.2f' % rand_dist(-1000,1000))

'''
PART V
In class we have discussed comparison operator ==
In Python there is also an identity operator id() which takes a single parameter - a reference to any object
Write a function both_equal() which tests whether the two objects have the same identity and are equal.
'''

def both_equal(obj, another):
    return (obj==another and id(obj)==id(another))

import fractions
f1 = fractions.Fraction(1,3)
f2 = fractions.Fraction(1,3)

print('############### Identity Checking #################')
print('Fractions: f1 = %s f2 = %s' % (f1, f2), both_equal(f1, f2), f1 == f2)

f3 = f1
print('Fractions: f1 = %s f3 = %s' % (f1, f3), both_equal(f1, f3), f1 == f3)

i1 = 4
i2 = 4
print('Integers: i1 = %s i2 = %s' % (i1, i2), both_equal(i1, i2), i1 == i2)

i3 = i1
print('Integers i1 = %s i3 = %s' % (i1, i3), both_equal(i1, i3), i3 == i1)

import decimal

d1 = decimal.Decimal('10.05')
d2 = decimal.Decimal('10.05')
print('Decimals d1 = %s  d2 = %s' % (d1, d2), both_equal(d1, d2), d1 == d2)