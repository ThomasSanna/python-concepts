# list of most importants built-in functions:


    # type()	Returns the type of an object

print('\n------type-------')

print(type(1)) # <class 'int'>
print(type(1.0)) # <class 'float'>
print(type('1')) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple'>
print(type({1, 2, 3})) # <class 'set'>
print(type({1: 'one', 2: 'two', 3: 'three'})) # <class 'dict'>
print(type(None)) # <class 'NoneType'>
print(type(type(1))) # <class 'type'>


    # int(), str(), float(), bool()

print('\n------int, str, float, bool-------')

print(type(1.0), 1.0, type(int(1.0)), int(1.0)) # <class 'float'> 1.0 <class 'int'> 1
print(type(1), 1, type(str(1)), str(1)) # <class 'int'> 1 <class 'str'> 1
print(type(1), 1, type(float(1)), float(1)) # <class 'int'> 1 <class 'float'> 1.0
print(type(1), 1, type(bool(1)), bool(1)) # <class 'int'> 1 <class 'bool'> True


    # list(), tuple(), set(), dict()
    
print('\n------list, tuple, set, dict-------')

print(list([1, 2, 3])) # [1, 2, 3]
print(tuple([1, 2, 3])) # (1, 2, 3)
print(set([1, 2, 3])) # {1, 2, 3}
print(dict([(1, 'one'), (2, 'two'), (3, 'three')])) # {1: 'one', 2: 'two', 3: 'three'}
print(dict (one=1, two=2, three=3)) # {'one': 1, 'two': 2, 'three': 3}

    # abs()	Returns the absolute value of a number

print('\n------abs-------')

print(abs(-7.25))
print(abs(2+3j)) 


    # all()	Returns True if all items in an iterable object are true

print('\n------all-------')

print(all([1, 2, 3, 4]))
print(all([0, 1, 2, 3, 4])) # 0 is false
print(all([1, 2, 3, 4, False])) # False is false


    # any()	Returns True if any item in an iterable object is true

print('\n------any-------')

print(any([1, 2, 3, 4, False])) # False is false
print(any([1, 2, 3, 4])) # True
print(any([0, False])) # False


    # max() / min() returns the largest/smallest value in an iterable

print('\n------max/min-------')

print(max([1, 2, 3, 4])) # 4
print(min([1, 2, 3, 4])) # 1

#with matrix :
print(max([1, 2, 3, 4], [5, 6, 7, 8])) # [5, 6, 7, 8]
print(min([1, 2, 3, 4], [5, 6, 7, 8])) # [1, 2, 3, 4]

#with null value:
print(max([1, 2, 3, 4], [5, 6, 7, 8], [])) # [5, 6, 7, 8]
print(min([1, 2, 3, 4], [5, 6, 7, 8], [])) # []


    # sum()	Returns the sum of all items in an iterable

print('\n------sum-------')

print(sum([1, 2, 3, 4])) # 10
print(sum([1, 2, 3, 4], 10)) # 20
# sum([1, 2, 3, 4], 10, 20) # TypeError: sum expected at most 2 arguments, got 3

#with matrix:
print(sum([[1, 2, 3, 4], [5, 6, 7, 8]][0])) # 10 (sum of first list)
print(sum([[1, 2, 3, 4], [5, 6, 7, 8]][1])) # 26 (sum of second list)

#with null value:
print(sum([])) # 0


    # len()	Returns the length of an object

print('\n------len-------')

print(len([1, 2, 3, 4])) # 4
print(len([[1, 2, 3, 4], [5, 6, 7, 8]])) # 2
print(len([])) # 0


    # round()   Rounds a numbers

print('\n------round-------')

print(round(5.76543, 2)) # 5.77
print(round(5.76543)) # 6


    # sorted()	Returns a sorted list

print('\n------sorted-------')

print(sorted([5, 2, 3, 1, 4])) # [1, 2, 3, 4, 5]
print(sorted([5, 2, 3, 1, 4], reverse=True)) # [5, 4, 3, 2, 1]

#with matrix:
print(sorted([[2, 1], [1, 2], [3, 3]], key=lambda x: x[0])) # [[1, 2], [2, 1], [3, 3]] (sort by first element)
print(sorted([[2, 1], [1, 2], [3, 3]], key=lambda x: x[1])) # [[2, 1], [1, 2], [3, 3]] (sort by second element)


    # enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object

print('\n------enumerate-------')

print(enumerate(['Hello', 'World', '!'])) # <enumerate object at 0x0000020F4F6F0A20> (memory address)
print(list(enumerate(['Hello', 'World', '!']))) # [(0, 'Hello'), (1, 'World'), (2, '!')]


    # format()	Formats a specified value
    
print('\n------format-------')

print(format(0.5, '%')) # 50.000000%
print(format(0.5, '.2%')) # 50.00%
print(format(0.5, '.2f')) # 0.50
print(format(0.5, '.0f')) # 1
print(format(0.5, '.0%')) # 50%
print(format(0.5, '.0e')) # 5e-01
print(format(0.5, '.0E')) # 5E-01


    # open(), read(), write(), close()	Opens, reads, writes and closes files

print('\n------open-------')

#in the terminal, cd to the folder where the file is located (cd python-concepts/built-in-functions)

file = open('test.txt', 'w') # w = write mode (other modes : r = read, a = append)
file.write('Hello World!')
file.close() # don't forget to close the file

#writing in append mode
file = open('test.txt', 'a') # a = append mode
file.write(f' [1, 2, 3, 4]')
file.write('\n [5, 6, 7, 8]')
file.close()

#reading
file = open('test.txt', 'r')
print(file.read()) # print the whole file
file.close()

file = open('test.txt', 'r')
print("first line :")
print(file.readline()) # print the first line
print("second line :")
print(file.readline()) # print the second line
file.close()

#reading with loop
file = open('test.txt', 'r')
for line in file:
    print(line)
file.close()

#reading with loop and removing \n
file = open('test.txt', 'r')
for line in file:
    print(line.rstrip())
file.close()