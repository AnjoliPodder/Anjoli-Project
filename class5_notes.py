'''
LISTS
'''

a_list = [1,2,3,"A string",1.5]     # python lists can contain objects of multiple types
a_list.append("something else")     # append adds to the end of the list
a_list.insert(0,"First")            # insert at a given index
len(a_list)                         # returns the number of items in a list
my_list = list(range(1,10,2))       # create a list from a range
new_list = a_list + my_list         # join two lists together
del my_list[0]                      # remove an item in the list at the given index
a_copy = my_list[:]                 # makes a copy of the list using slicer
one_more_copy = my_list.copy()      # another way to make a copy
3 in my_list                        # returns True if the item is in the list

for el in a_copy:
    print(el, end = ',')            # iterate through the list
print ("\n")

for el in range(0,len(a_copy)):     # iterate using range
    print(el, a_copy[el])

for ix, el in enumerate(a_copy):    # enumerate function keeps track of both the item and the index
    print(ix, el)

list2 = [1] * 3                     # create a list of 3 integers
string2 = '#' * 10                  # create a string with 10 hashes


list_of_lists = [list2] * 4         # create a list of lists
del list2[-1]
list_of_lists                       # notice that if the reference variable changes, the list of lists changes too
list_of_lists[1] = list_of_lists[1].copy()  # make a copy of the list to prevent changes like the above

new_l = list(range(1,21))
print(new_l[:10])                   # returns the first 10 items in the list
print(new_l[0:10:2])                # third argument can be added as a step
print(new_l[::-1])                  # reverses the list
print(new_l[-10:])                  # last 10 elements of the list

# example - create a list of numbers from 1 to 20, every 3rd number
# print the square of each element in the list
numbers = list(range(1,20,3))
for i in numbers:
    print("The square of", i, "is", i**2)

# Take the string "Trump is president elect", jumble the characters

import random
my_string = "Trump is president elect!"
result = [''] * len(my_string)
for ix in range(0,len(my_string)):
    r = random.choice(my_string)
    result[ix] = r
    my_string2 = my_string.replace(r,"",1)
print(''.join(result))


Test = "EEMMCC"
Test.replace("E","",1)









