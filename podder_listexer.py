
'''

'''

'''
PART I - Nucleic Acid
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is
formed by replacing all occurrences of 'T' in tt with 'U' in uu.
Given: A DNA string tt having length at most 1000 nt.
Return: The transcribed RNA string of tt.

Sample input: GATGGAACTTGACTACGTAAATT
Sample output: GAUGGAACUUGACUACGUAAAUU
'''

# one solution using the replace function for strings


def transcribe(tt):
    return tt.replace("T", "U")

print(transcribe("GATGGAACTTGACTACGTAAATT"))

# another solution using a for loop


def transcribe2(tt):
    uu = ""
    for ch in tt:
        if ch == "T":
            uu += "U"
        else:
            uu += ch
    return uu

print(transcribe2("GATGGAACTTGACTACGTAAATT"))

print(transcribe("GATGGAACTTGACTACGTAAATT") == transcribe2("GATGGAACTTGACTACGTAAATT"))

'''
PART II - Gymnast Scores
A gymnast can earn a score between 1 and 10 from each judge; nothing lower, nothing higher.
All scores are integer values; there are no decimal scores from a single judge.
Store the possible scores a gymnast can earn from one judge in a tuple.
Print out the sentence, "The lowest possible score is ___, and the highest possible score is ___."
Use the values from your tuple.
'''
scores = tuple(range(1, 11))
print("The lowest possible score is %d and the highest possible score is %d." % (min(scores), max(scores)))

'''
PART III - Max, Min, Average, and Sum
Given an input_list  calculate the largest, the smallest, the mean and the sum of all elements in the list
Do the same for the first 15 elements
Do the same for the last 15 elements
Print out the results using %d notation.
'''

input_list = [33,
 104,
 95,
 59,
 29,
 92,
 91,
 20,
 101,
 32,
 77,
 21,
 21,
 54,
 14,
 105,
 98,
 52,
 89,
 93,
 46,
 74,
 91,
 25,
 73,
 48,
 99,
 21,
 15,
 44,
 12,
 101,
 69,
 38,
 52,
 99,
 103,
 17,
 99,
 12,
 11,
 71,
 21,
 37,
 82,
 68,
 18,
 71,
 59,
 13]

# calculations on the whole list


largest = max(input_list)
smallest = min(input_list)
mean = sum(input_list)/len(input_list)
total = sum(input_list)

print("The largest in the list is %d, the smallest is %d, the mean is %4.2f and the sum is %d" % (largest, smallest, mean, total))

# calculations on the first 15 items in the list


largest_15 = max(input_list[:15])
smallest_15 = min(input_list[:15])
mean_15 = sum(input_list[:15])/len(input_list[:15])
total_15 = sum(input_list[:15])

print("The largest in the first 15 items in the list is %d, the smallest is %d, the mean is %4.2f and the sum is %d" % (largest_15, smallest_15, mean_15, total_15))

# calculations on the last 15 items in the list


largest_last15 = max(input_list[-15:])
smallest_last15 = min(input_list[-15:])
mean_last15 = sum(input_list[-15:])/len(input_list[-15:])
total_last15 = sum(input_list[-15:])

print("The largest in the last 15 items in the list is %d, the smallest is %d, the mean is %4.2f and the sum is %d" % (largest_last15, smallest_last15, mean_last15, total_last15))


'''
PART IV
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward
https://en.wikipedia.org/wiki/Palindrome
Write a functions is_palindrome() which checks if the input string is a palindrome.
'''

def palindrome(word):
    return word == word[::-1]

print(palindrome("tacocat"))
print(palindrome("taco cat"))
print(palindrome("Mr Owl ate my metal worm"))
print(palindrome("random string"))

# another definition for a palindrome function that ignores whitespace and is case insensitive

def palindrome2(word):
    stripped = word.replace(" ","").lower()
    return stripped == stripped[::-1]

print(palindrome2("tacocat"))
print(palindrome2("taco cat"))
print(palindrome2("Mr Owl ate my metal worm"))
print(palindrome2("random string"))

