"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math


A = 'task02a.txt'
B = 'task02b.txt'
C = 'task02c.txt'
fileA = open(A, 'r')
fileB = open(B, 'r')
fileC = open(C, 'r')

dataA = fileA.read()
dataB = fileB.read()
dataC = fileC.read()

listA = dataA.split('\n')
listB = dataB.split('\n')
listC = dataC.split('\n')

number=[]
rightTris=[]


for i in enumerate(listA):
    number.append(i[1])
    if i[1] == "":
        a=int(number[0])
        b=int(number[1])
        c=int(number[2])
        if c**2+a**2==b**2:
            rightTris.append(b**2)
        if a**2+b**2==c**2:
            rightTris.append(c**2)
        if c**2+b**2==a**2:
            rightTris.append(a**2)
        number.clear()
    else:
        print("")
    if number==['65', '48', '45']:
        aRights = rightTris.index((rightTris[-1]))+1
        break
rightTris.clear()
for i in enumerate(listB):
    number.append(i[1])
    if i[1] == "":
        a=int(number[0])
        b=int(number[1])
        c=int(number[2])
        if c**2+a**2==b**2:
            rightTris.append(b**2)
        if a**2+b**2==c**2:
            rightTris.append(c**2)
        if c**2+b**2==a**2:
            rightTris.append(a**2)
        number.clear()
    else:
        print("")
    if number==['28', '45', '53']:
        bRights = rightTris.index((rightTris[-1]))+1
        break
rightTris.clear()
for i in enumerate(listC):
    number.append(i[1])
    if i[1] == "":
        a=int(number[0])
        b=int(number[1])
        c=int(number[2])
        if c**2+a**2==b**2:
            rightTris.append(b**2)
        if a**2+b**2==c**2:
            rightTris.append(c**2)
        if c**2+b**2==a**2:
            rightTris.append(a**2)
        number.clear()
    else:
        print("")
    if number==['30', '24', '19']:
        cRights = rightTris.index((rightTris[-1]))+1
        break
print(f'task02a has {aRights} right triangles\ntask02b has {bRights} right triangles\ntask02c has {cRights} right triangles\n')

