'''
DICTIONARIES
'''

my_d = {}  # curly brackets are used to denote a dictionary
my_dict = {'name': 'Hillary',
           'is_president': False,
           'gender': 'female'}

another_d = dict()  # creates an empty dictionary.
                    # You can add an argument that is a list of tuples to create a dictionary from them

my_dict.keys  # returns a list of keys
my_dict.values  # returns a list of values

actors = [('act1', 'Brad Pitt'), ('act2', 'Michael Caine')]
actor_dict = dict(actors)

actor_dict['act3'] = 'Angelina Jolie'  # add another entry
actor_dict['act2']  # returns the value of the given key
del actor_dict['act2']  # deletes an item from the dictionary

a1 = [1,2,3,4]
a2 = ["one", "two","three", "four"]

zipped = dict(zip(a1, a2))  # zip connects list 1 and list 2 element-wise. Can be used to create a dictionary

'''
# Ex 1
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
'''

input_text = '''In every program that we have talked about so far, when the program ends, the computer forgets everything
that happened in the program. Every variable you created, every string you used, every Boolean, every
list-it’s all gone. But what if you want to keep some of the data that you generate in a program, and save
it for when you run the program later? Or, maybe you want to save some data so that a different program
could use the data that you generated.'''



def frequency(sentence, top_n = 5):  # top_n allows the user to specify the top number of items to return from the
    if (type(sentence) != type(str())):
        raise ValueError("Expecting a string. Got an object of %s" % type(sentence))
    else:
        freq_dict = {}
        spl = sentence.lower().split()
        for word in spl:
            if not (word in freq_dict):
                freq_dict[word] = 1
            else:
                freq_dict[word] += 1
        # add some sorting functionality!

        # dictionary can't be sorted - convert to a list of tuples. Value first, key second because sort sorts by the first element in the tuple
        freq_list = []
        for k in freq_dict.keys():
            freq_list.append((freq_dict[k], k))
        freq_list.sort(reverse=True)
    return freq_list[:top_n]

print(frequency(input_text))
# print(frequency(123))


'''
Ex 2
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
Modification: running amount, i.e. current balance at each transaction
'''
deposit_log = '''D 100
W 200
D 300
W HUNDRED
D 300
W 200
D 100
D 100
D ZERO
W 300'''

'''

#clumsier version of the solution - without error handling

def net_amount(log):
    spl = log.split()
    plus = True
    count = 0
    for s in spl:
        if s == "D":
            plus = True
        elif s == "W":
            plus = False
        elif plus:
            count += int(s)
        else:
            count -= int(s)
    return count
'''

# another solution using an enumerator
def net_amount2(log):
    spl = log.split()
    count = 0
    invalids = []
    for idx, s in enumerate(spl):
        if idx%2 == 0:
            if s == "D":
                try:
                    count += int(spl[idx+1])
                except:
                    invalids.append((spl[idx], spl[idx + 1]))
            elif s == "W":
                try:
                    count -= int(spl[idx + 1])
                except:
                    invalids.append((spl[idx], spl[idx + 1]))
    print("Invalid Transactions:")
    [print(i) for i in invalids]
    return count

# print("The total balance is %d" % net_amount(deposit_log))
print("The total balance is %d" % net_amount2(deposit_log))

'''
Ex 4:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be (i+1)*(j+1).
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

'''

def matrix (x, y):
    m = []
    for in1 in range(1, x + 1):
        row = []
        for in2 in range(1, y + 1):
            row.append(in1 * in2)
        m.append(row)
    return m

print(matrix(3,5))

'''
Modification 1:
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
'''

def matrix2 (x, y):
    m = []
    for in1 in range(0, x):
        row = []
        for in2 in range(1, y + 1):
            row.append(in1 * y + in2)
        m.append(row)
    return m

print(matrix2(3,5))

'''
Modification 2: transpose the list
'''

def transpose (matrix):
    if matrix == []:
        return []
    else:
        m = []
        for in1 in range(0, len(matrix[0])):
            row = []
            for in2 in range(0, len(matrix)):
                row.append(matrix[in2][in1])
            m.append(row)
        return m

print(transpose(matrix(3,5)))
print(transpose(matrix2(3,5)))









