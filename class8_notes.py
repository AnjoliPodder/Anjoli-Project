'''
File I/O
https://drive.google.com/drive/u/0/folders/0Bz33uEu_6ayddDd5bG9lcC1xVzA
https://docs.python.org/3/library/io.html
'''

import io
import os.path

# get the current working directory

os.getcwd()

# set the filepath for the target file

filepath = 'C:\\Users\\Anjoli\\PycharmProjects\\pyintro_stu\\NASA_access_log_Jul95_1000.txt'

# open the file

fd = open(filepath, mode='rt')

# print the first line

for line in fd:
    print(line)
    break

# seek method takes two arguments. 1 - relative position, 2 - relative to what?. SEEKSET sets the pointer to position 0
# where 0 is the first char

fd.seek(0, io.SEEK_SET)

# returns the current position in the file

fd.tell()

# reads the rest of the line from the current position onwards

fd.readline()

for idx, line in enumerate(fd):
    print(line)
    if idx > 10:
        break

# close the file
fd.close()

filepath = 'C:\\Users\\Anjoli\\PycharmProjects\\pyintro_stu\\NASA_access_log_Jul95_1000.txt'
allText = None
with open (filepath, mode = 'rt') as fd:
    allText = fd.readlines()
    count = 0
    for line in allText:
        tokens = line.split(' ')
        if int(tokens[-2]) != 200:
            count += 1
print("Number of ties web users got response other than HTTP_OK was %d" % count)

# print the top 5 most used resources according to the log

filepath = 'C:\\Users\\Anjoli\\PycharmProjects\\pyintro_stu\\NASA_access_log_Jul95_1000.txt'
allText = None
with open (filepath, mode = 'rt') as fd:
    allText = fd.readlines()
    resource_dict = {}
    for line in allText:
        tokens = line.split(' ')
        resource = tokens[-4]
        if resource in resource_dict.keys():
            resource_dict[resource]+=1
        else:
            resource_dict[resource]=1
tup = resource_dict.items()
swap_tup = [(v, k) for k, v in tup]
swap_tup.sort(reverse=True)
for i in swap_tup[:5]:
    print (i)


# using exception handling - create a file with random chars for 10 lines in a new file some.txt

import random
fd = None
filepath2 = 'C:\\Users\\Anjoli\\PycharmProjects\\pyintro_stu\\some.txt' # file does not exist - will create if not there
try:
    fd = open(filepath2, mode = "wt") # mode wt means write, text mode
    for _ in range(1,11):
        text = " ".join([chr(random.randint(80,120)) for _ in range(1,200)])
        print(text, file = fd)
    fd.flush()      # force write to disk - not always necessary
except Exception as ex:
    print("Error occurred %s" % ex)
finally:
    if not(fd is None):
        fd.close()

# append to an existing file

import random
fd = None
filepath2 = 'C:\\Users\\Anjoli\\PycharmProjects\\pyintro_stu\\some.txt' # file does not exist - will create if not there
try:
    fd = open(filepath2, mode = "a+")  # mode a+ tells python to APPEND to the existing file. mode wt would replace existing text
    for _ in range(1,11):
        text = " ".join([chr(random.randint(80,120)) for _ in range(1,200)])
        print(text, file = fd)
    fd.flush()      # force write to disk - not always necessary
except Exception as ex:
    print("Error occurred %s" % ex)
finally:
    if not(fd is None):
        fd.close()

# write in byte mode

import random
fd = None
filepath2 = 'C:\\Users\\Anjoli\\PycharmProjects\\pyintro_stu\\some.bin' # file does not exist - will create if not there
encoding = 'UTF-8'
try:
    fd = open(filepath2, mode = "wb") # mode wb means write, byte mode
    print(bytes("="*200, encoding = encoding), file=fd)
    for _ in range(1,11):
        text = " ".join([chr(random.randint(80,120)) for _ in range(1,200)])
        print(bytes(text, encoding = encoding), file = fd)
    fd.flush()      # force write to disk - not always necessary
except Exception as ex:
    print("Error occurred %s" % ex)
finally:
    if not(fd is None):
        fd.close()

# initialize a table

import pprint
tbl = [[None]*5 for _ in range(1,4)]
for ix in range(len(tbl)):
    for ik in range(len(tbl[ix])):
        tbl[ix][ik] = (ix+1)*(ik+1)
pprint.pprint(tbl)

# render a table in HTML using memory buffers - more efficient than using strings

import io
mem = io.StringIO()
mem.write('<table>')
for ix in range(len(tbl)):
    mem.write('<tr>')
    for ik in range(len(tbl[ix])):
        mem.write('<td>')
        mem.write(str(tbl[ix][ik]))
        mem.write('</td>')
    mem.write('</tr>')
mem.write('</table>')

with io.open('table_one.html', 'w') as fd:
    mem.seek(0)
    fd.write(mem.read()) # read and write the entire buffer
mem.close()

'''
FILE AND DIRECTORY EXERCISES
'''

import os.path
os.path.isdir(os.getcwd()) # returns True if this is a directory
os.listdir(os.getcwd()) # returns a list of filenames in this directory

# count the files in a directory

root = os.getcwd()
file_cnt = 0
for fn in os.listdir():
    fullPath = os.path.join(root, fn)
    print(fullPath)
    if os.path.isdir(fullPath):
        print("This is a directory %s" % fullPath)
    elif os.path.isfile(fullPath):
        file_cnt += 1
print("Number of files in %s is %d" %(root, file_cnt))

# count the files in a directory - recursively through subdirectories

def recursive_filecount(path):
    file_cnt = 0
    for fn in os.listdir(): # change this line - it is currently reading the files in the current directory - need to change to read target
        fullPath = os.path.join(path, fn)
        print(fullPath)
        if os.path.isdir(fullPath):
            print("This is a directory %s" % fullPath)
            file_cnt += recursive_filecount(fullPath)
        elif os.path.isfile(fullPath):
            file_cnt += 1
    print("Number of files in %s is %d" %(path, file_cnt))
    return file_cnt

print(recursive_filecount('C:\\Users\\Anjoli\\PycharmProjects'))


'''
PICKLE MODULE
'''

'''
import pickle

fd = open("some_objects.dat", "rb")
tbl = pickle.load(fd)
someFunc = pickle.load(fd)

import pprint
pprint.pprint(tbl)
someFunc()
'''



