#!/usr/bin/env python
# lists.py
# https://docs.python.org/2/tutorial/datastructures.html

# Files to work with
file1 = 'list1.txt'
file2 = 'list2.txt'
outfile = 'output.txt'

# take "file1" and "file2" and read them in as seperate lists
# the rstrip() method is used to remove newline characters from the end of each line
l1 = [line.rstrip('\r\n') for line in open(file1)]
l2 = [line.rstrip('\r\n') for line in open(file2)]

# print both lists
print("List 1: " + str(l1))
print("List 2: " + str(l2))

# print the length of l1
print("List 1 length: " + str(len(l1)))

# print info about list indexing
print("Python starts counting at 0")
print("List 1, index location 0: " + str(l1[0]))
print("List 1, index location 3: " + str(l1[3]))

# make sure both lists are the same length
if len(l1) != len(l2):
    print("Lists are not equal length. Exiting!")
    exit()

# open the output file
o = open(outfile, 'w')

# iterate through both lists
for a, b in zip(l1, l2):
    # write each item from both lists to the same line, seperated by a comma
    o.write(a + ", " + b + "\n")

# close the output file
o.close()
