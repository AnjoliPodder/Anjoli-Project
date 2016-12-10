'''
HW01
'''


'''
Part 1
Write an expression which computes post-money valuation of a business using the following formula
post  mooney  = pre money  +  investor cash

A. Use objects of class Decimal to perform this calculation with
pre money       = 75.20
investor cash   = 15.50
'''

import fractions
pre_money = fractions.Decimal(75.20)
investor_cash = fractions.Decimal(15.50)
post_money=pre_money+investor_cash

'''
B. Use objects of class float to perform this calculation
pre money       = 75.20
investor cash   = 15.50
'''

pre_money2 = 75.20
investor_cash2 = 15.50
post_money2=pre_money2+investor_cash2

'''
C. Compare two results using equality operator
'''
post_money==post_money2

'''

D. Use type conversion function float() applied to the result of type Decimal
 and then compare converted value with the float value
'''
float(post_money)==post_money2


'''
Part 2
A PE firm Vista Enterprises has three founders who have corresponding number of ordinary shares in a firm
300,000   - founder 1
300,000   - founder 2
400,000   - founder 3
The total enterprise value in shares is simply a sum of shares of all founders.
Calculate total enterprise value and the percentage ownership for each founder
as founder's number of shares divided by total enterprise value.
'''
print("Part 2")
founder1 = 300000
founder2 = 300000
founder3 = 400000
total_value=founder1+founder2+founder3
print("Total Value Is $" + str(total_value))
percent1 = founder1/total_value
print("Founder 1 Percent Is " + str(percent1))
percent2 = founder2/total_value
print("Founder 2 Percent Is " + str(percent2))
percent3 = founder3/total_value
print("Founder 3 Percent Is " + str(percent3))

'''
Write an expression which tests whether founder 1 and founder 2 have equal percentage of shares.
Use print() function to show the result of each calculation.
'''
print("Founder 1 and 2 have equal shares? " +str(percent1==percent2))

'''
Part 3
Calculate the length of hypotenuse in a right angled triangle
given that  variables a_side and b_side are the length of the other two sides.
Use Pythagorean theorem
https://en.wikipedia.org/wiki/Pythagorean_theorem
Calculate the result for the following pairs of values for a_side and b_side
Use exponentiation operator only, do not use math.sqrt()

3       4
10.5    6.5
1       3
print the result of each calculation using print() function
'''

print("Part 3")
def hypotenuse(a_side,b_side):
    c_side=(a_side**2+b_side**2)**(1/2)
    return c_side;
print(hypotenuse(3,4))
print(hypotenuse(10.5,6.5))
print(hypotenuse(1,3))



'''
Part 4
instantiate two variables of type Fraction
6/4 and 2/4, subtract  2/4 from 6/4 and print the result.
'''
print("Part 4")
f1 = fractions.Fraction(6,4)
f2 = fractions.Fraction(2,4)
f3=f1-f2
print(f3)
