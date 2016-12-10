def count_vowels(input):
    count = 0
    for ch in input:
        if ch.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("aeiou"))
print(count_vowels("The quick brown fox jumps over the lazy dog"))
print(count_vowels("ThIS Is a MiXeD CASE SeNTEnce"))

'''
Write a function which calculates the sum of product of two numbers x and y where x takes on values between 50 and 60
inclusive and y takes on values between 10 and 20 inclusive. Hence, your result will be:
50*10 + 50*11 + ... + 50*20 + 51*10 + 51*11 + ... +51*20 + ... + 60*10 + 60*11 + ... + 60*20
'''

def sum_of_product():
    x = list(range(50, 61))
    y = list(range(10, 21))
    total = 0
    for el in x:
        for el2 in y:
           # print("multiplying", el, "and", el2)    #added for testing purposes
            total += el * el2
    return total

print(sum_of_product())
print(sum_of_product() == sum(range(50, 61)) * sum(range(10, 21)))

