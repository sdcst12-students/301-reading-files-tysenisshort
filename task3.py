#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.
For sample data task03.txt, the largest sum should be 68787
"""
def sumOfValues():
    filename = 'task03.txt'
    file = open(filename,'r')
    data = file.read()
    myList = data.split('\n')
    otherlist = []
    numbers = []
    for i in myList:
        if i != "":
            i = int(i)
            otherlist.append(i)
        if i == "":
            numbers.append(sum(otherlist))
            otherlist = []
    numbers.sort()
    largest = numbers[-1]
    print(largest)
sumOfValues()