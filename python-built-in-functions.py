# List of most importants built-in functions:

print("------------------BUILT-IN FUNCTIONS------------------")

    # print()	Prints to the standard output device -----------------------------------

print('\n------print-------')

print('Hello World!') # Hello World!
x = 5
print('x is', x) # x is 5
print(f"x is {x}") # x is 5 (f-string)
print('x is ' + str(x)) # x is 5 (concatenation)


    # type()	Returns the type of an object -----------------------------------

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


    # int(), str(), float(), bool() -----------------------------------

print('\n------int, str, float, bool-------')

print(type(1.0), 1.0, type(int(1.0)), int(1.0)) # <class 'float'> 1.0 <class 'int'> 1
print(type(1), 1, type(str(1)), str(1)) # <class 'int'> 1 <class 'str'> 1
print(type(1), 1, type(float(1)), float(1)) # <class 'int'> 1 <class 'float'> 1.0
print(type(1), 1, type(bool(1)), bool(1)) # <class 'int'> 1 <class 'bool'> True


    # list(), tuple(), set(), dict() -----------------------------------
    
print('\n------list, tuple, set, dict-------')

print(list([1, 2, 3])) # [1, 2, 3]
print(tuple([1, 2, 3])) # (1, 2, 3) 
print(set([1, 2, 3])) # {1, 2, 3}
print(dict([(1, 'one'), (2, 'two'), (3, 'three')])) # {1: 'one', 2: 'two', 3: 'three'}
print(dict (one=1, two=2, three=3)) # {'one': 1, 'two': 2, 'three': 3}

    # abs()	Returns the absolute value of a number -----------------------------------

print('\n------abs-------')

print(abs(-7.25))
print(abs(2+3j)) 


    # all()	Returns True if all items in an iterable object are true ------------------

print('\n------all-------')

print(all([1, 2, 3, 4]))
print(all([0, 1, 2, 3, 4])) # 0 is false
print(all([1, 2, 3, 4, False])) # False is false


    # any()	Returns True if any item in an iterable object is true ------------------

print('\n------any-------')

print(any([1, 2, 3, 4, False])) # False is false
print(any([1, 2, 3, 4])) # True
print(any([0, False])) # False


    # max() / min() returns the largest/smallest value in an iterable -----------------------------------

print('\n------max/min-------')

print(max([1, 2, 3, 4])) # 4
print(min([1, 2, 3, 4])) # 1

#with matrix :
print(max([1, 2, 3, 4], [5, 6, 7, 8])) # [5, 6, 7, 8]
print(min([1, 2, 3, 4], [5, 6, 7, 8])) # [1, 2, 3, 4]

#with null value:
print(max([1, 2, 3, 4], [5, 6, 7, 8], [])) # [5, 6, 7, 8]
print(min([1, 2, 3, 4], [5, 6, 7, 8], [])) # []


    # sum()	Returns the sum of all items in an iterable -----------------------------------

print('\n------sum-------')

print(sum([1, 2, 3, 4])) # 10
print(sum([1, 2, 3, 4], 10)) # 20
# sum([1, 2, 3, 4], 10, 20) # TypeError: sum expected at most 2 arguments, got 3

#with matrix:
print(sum([[1, 2, 3, 4], [5, 6, 7, 8]][0])) # 10 (sum of first list)
print(sum([[1, 2, 3, 4], [5, 6, 7, 8]][1])) # 26 (sum of second list)

#with null value:
print(sum([])) # 0


    # len()	Returns the length of an object -----------------------------------

print('\n------len-------')

print(len([1, 2, 3, 4])) # 4
print(len([[1, 2, 3, 4], [5, 6, 7, 8]])) # 2
print(len([])) # 0


    # round()   Rounds a numbers -----------------------------------

print('\n------round-------')

print(round(5.76543, 2)) # 5.77
print(round(5.76543)) # 6


    # range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default) -----------------------------------
    
print('\n------range-------')

print(range(10)) # range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    # sorted()	Returns a sorted list -----------------------------------

print('\n------sorted-------')

print(sorted([5, 2, 3, 1, 4])) # [1, 2, 3, 4, 5]
print(sorted([5, 2, 3, 1, 4], reverse=True)) # [5, 4, 3, 2, 1]

#with matrix:
print(sorted([[2, 1], [1, 2], [3, 3]], key=lambda x: x[0])) # [[1, 2], [2, 1], [3, 3]] (sort by first element)
print(sorted([[2, 1], [1, 2], [3, 3]], key=lambda x: x[1])) # [[2, 1], [1, 2], [3, 3]] (sort by second element)


    # reversed()	Returns a reversed iterator -----------------------------------

print('\n------reversed-------')

print(reversed([1, 0, 5, 2])) # <list_reverseiterator object at 0x0000020F4F6F0A20> (memory address)
print(list(reversed([1, 0, 5, 2]))) # [2, 5, 0, 1]


    # zip()	Returns an iterator, from two or more iterators -----------------------------------

print('\n------zip-------')

print(zip([1, 2, 3], [4, 5, 6])) # <zip object at 0x0000020F4F6F0A20> (memory address)
print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]))) # [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]


    # enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object -----------------------------------

print('\n------enumerate-------')

print(enumerate(['Hello', 'World', '!'])) # <enumerate object at 0x0000020F4F6F0A20> (memory address)
print(list(enumerate(['Hello', 'World', '!']))) # [(0, 'Hello'), (1, 'World'), (2, '!')]


    # filter()	Use a filter function to exclude items in an iterable object -----------------------------------
    
print('\n------filter-------')

def is_even(x):
    return x % 2 == 0

print(filter(is_even, [1, 2, 3, 4, 5, 6])) # <filter object at 0x0000020F4F6F0A20> (memory address)
print(list(filter(is_even, [1, 2, 3, 4, 5, 6]))) # [2, 4, 6]
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))) # [2, 4, 6]


    # map()	Use a map function to execute a specified function for each item in an iterable. The item is sent to the function as a parameter. -----------------------------------
    
print('\n------map-------')

def square(x):
    return x * x

print(map(square, [1, 2, 3, 4, 5, 6])) # <map object at 0x0000020F4F6F0A20> (memory address)
print(list(map(square, [1, 2, 3, 4, 5, 6]))) # [1, 4, 9, 16, 25, 36]
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))) # [1, 4, 9, 16, 25, 36]

    # format()	Formats a specified value -----------------------------------
    
print('\n------format-------')

print(format(0.5, '%')) # 50.000000% (string)
print(format(0.5, '.2%')) # 50.00% (string)
print(format(0.5, '.2f')) # 0.50 (string)
print(format(0.5, '.0e')) # 5e-01 (string)


    # bin()	Returns the binary version of a number -----------------------------------
    
print('\n------bin-------')

print(bin(5)) # 0b101 (string)
print(bin(5)[2:]) # 101 (string)


