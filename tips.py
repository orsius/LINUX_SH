#!/usr/local/bin/python3.5

#import numpy as np 
#import panda as pd

"""
# Open a file: file
file = open('moby_dick.txt', 'r')
# Print it
print(file.read())
# Check whether file is closed
print(file.closed)
# Close file
file.close()


# Assign filename: file
file = 'titanic_corrupt.txt'
# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])
# Print the head of the DataFrame
print(data.head())
"""

rf = open("api_query.2016-12-04.log")
wf = open("newwordlist.txt","w")
"""
for line in rf:
    newline = line.rstrip('\r\n')
    wf.write(newline)
    wf.write('\n')  # remove to leave out line breaks
rf.close()
wf.close()
"""



hand = open('mbox-short.txt')
"""
for line in hand:
    line = line.rstrip()
    if line.find('And ') >= 0:
        print(line)
"""
import re

for line in hand:
    line = line.rstrip()
    if re.search('^Okay', line) :
        print(line)
z = 'To dry.super@store.lu Sat Jan 5 09:14:16 2016'
x = '42 superdry girls eat a 3 bols of potatoe soup @9pm during wearing their sport shirt with the value 83 on iti. dry.super@store.lu'
y = re.findall('[0-9]+', x)
print(y)

g = re.findall('^To (\S+@\S+)' ,z)
print(g)

qpfile = open('api_query.2016-12-04.log', 'r')
"""
for line in qpfile:
    line = line.rstrip()
    if re.search('(ES\([0-9]+\)={)', line) :
    print(line)
"""
rf = open("api_query.2016-12-04.log")
wf = open("newwordlist.txt","w")
for line in rf:
    newline = line.rstrip('\r\n')
    wf.write(newline)
    wf.write('\n')  # remove to leave out line breaks
rf.close()
wf.close()
