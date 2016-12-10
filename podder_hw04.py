
'''
Write a function called merge_unique()
The function takes two lists of comparable objects, i.e. integers or strings or something like that
and combines them into new list with unique values, i.e. no duplicates. The new list is returned.
Return an empty list if objects passed down into this function are not lists.
Implement using for loops, then use sets , i.e. set object to achieve the same. The results should
be identical
'''

def merge_unique(a_list, b_list):
    if not(type(a_list)==type(list())) or not(type(b_list)==type(list())):
        return []
    else:
        unique = []
        for el in a_list + b_list:
            if el not in unique:
                unique.append(el)
        return unique

# Alternate method using sets

def merge_unique_alt(a_list, b_list):
    if not(type(a_list)==type(list())) or not(type(b_list)==type(list())):
        return []
    else:
        return set(a_list + b_list)

set1 = [1,2,3,4,5]
set2 = [3,4,5,6,7]
set3 = "Chicken"

print(merge_unique(set1, set2))
print(merge_unique_alt(set1, set2))
print(merge_unique(set1, set3))
print(merge_unique_alt(set1, set3))

'''
With a given integer number n_max, write a function gen_dict_square() to generate a dictionary that contains i as key and  i*i
as value for all odd i
such that  an integer number i between 1 and n_max (both included).
Function must return constructed dictionary. Use list comprehensions when applicable.
'''
def gen_dict_square(n_max):
    return dict([(x, x**2) for x in range(1, n_max+1, 2)])

print(gen_dict_square(10))
print(gen_dict_square(20))

'''
Write a function str_dup_cleaner() that accepts a sequence of whitespace separated words as input
and returns the list of words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:

'hello world and practice makes perfect and hello world again'

Then, the output should be:
'again and hello makes perfect practice world'

'''

def str_dup_cleaner(mult_lines):
    return " ".join(sorted(set(mult_lines.split())))

input = 'hello world and practice makes perfect and hello world again'
print(str_dup_cleaner(input))

'''
Define a function check_number() that can accept an integer number as input and returns the
"even" if the number is even, otherwise returns "odd".

Modification: dynamically detect whether an input to the function check_number() is an int
or a list of int. Raise exception if it is neither. Use lambda function to return a list of
["odd", "even", ...] if  an input is a list
If an input is an integer number return  a list of length one.
'''

def check_number(num_to_check):
    if num_to_check%2 == 0:
        return "even"
    else:
        return "odd"

print(check_number(7))
print(check_number(16))

def check_number_alt(num_to_check):
    f = lambda x: "even" if x % 2 == 0 else "odd"
    if type(num_to_check) == type(int()):
        return [f(num_to_check)]
    else:
        try:
            return [f(x) for x in num_to_check]
        except:
            raise ValueError("Invalid input type")

print(check_number_alt(7))
print(check_number_alt(16))
print(check_number_alt([16, 7, 8, 9]))
# print(check_number_alt([1,2,3,"text"]))
# print(check_number_alt("hey"))


'''
Write a function letters_and_digits() that accepts a sentence and calculates
the number of letters and digits and returns these two counts.
Suppose the following input is supplied to the function:
hello world! 123
Then, the function should  return 10, 3

Which means:
LETTERS 10
DIGITS 3
'''

def letters_and_digits(in_text):
    letter_count = 0
    number_count = 0
    for ch in in_text:
        if ord(ch) >= ord("a") and ord(ch) <= ord("z") or ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
            letter_count += 1
        elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
            number_count += 1
    return letter_count, number_count

print(letters_and_digits('hello world! 123'))
print(letters_and_digits('109hello 566&^%world!'))


# alternate version using embedded lambda functions - and learning how to chain comparisons

def letters_and_digits_alt(in_text):
    is_letter = lambda x: ord("a") <= ord(x) <= ord("z") or ord("A") <= ord(x) <= ord("Z")
    is_number = lambda x: ord("0") <= ord(x) <= ord("9")
    return [is_letter(x) for x in in_text].count(True), [is_number(x) for x in in_text].count(True)

print(letters_and_digits_alt('hello world! 123'))
print(letters_and_digits_alt('109hello 566&^%world!'))

# alternate super ugly one line version

def letters_and_digits_alt2(in_text):
    return [(ord("a") <= ord(x) <= ord("z") or ord("A") <= ord(x) <= ord("Z")) for x in in_text].count(True), \
           [(ord("0") <= ord(x) <= ord("9")) for x in in_text].count(True)

print(letters_and_digits_alt2('hello world! 123'))
print(letters_and_digits_alt2('109hello 566&^%world!'))