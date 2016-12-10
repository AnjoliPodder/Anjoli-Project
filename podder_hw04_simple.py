''''''

'''
Create a sorted list from the following list of 2-tuples by the second element of each tuple.
The original list should be left intact.
Hint: you could use list comprehension and lambda function
Hint:
'''
indata = [
  ('a', 0),
  ('b', 2),
  ('c', 1),
]

def sort_tuples(input):
    reversed = [(b, a) for a, b in input]
    reversed.sort()
    return [(b, a) for a, b in reversed]

print(sort_tuples(indata))

'''
Count the number of unique values in a list
'''
import random
indata = [random.randrange(100) for it in range(20)]

def count_unique(num_list):
    unique_ints = []
    for i in num_list:
        if not(i in unique_ints):
            unique_ints.append(i)
    return len(unique_ints)

print(indata)
print(count_unique(indata))


'''
Check if there is a key called city in stuff dictionary
If it does not exit, add new key/value pair to the dictionary
Add another key/value pair using key 'weight' and some float value
Delete key/value pair where key is 'weight'
'''
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print('city' in stuff.keys())
stuff['weight'] = 181.5
print(stuff)
del stuff['weight']
print(stuff)

'''
print the type of the value under key 'silly' in a_dict dictionary
create a copy of the  object stored under the key 'silly' and store it
in a_dict under key 'goose'
'''
a_dict = {4: "hi", True: 24, "silly": ["very", "very", "very"]}
print(type(a_dict['silly']))
a_dict['goose'] = a_dict['silly'][:]


'''
Iterate through python_words dictionary keys and values from the python_words dictionary
'''
python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

for key in python_words.keys():
    print(key, python_words.get(key))