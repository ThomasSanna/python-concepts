#Python Conditions Tutorial by WadeeKT

    # Bool Algebra ------------------------------------
print('\n -----------------BOOL ALGEBRA------------------- \n')

print('True and False : ', True and False)
print('True or False : ', True or False)

print('\nTrue and not False : ', True and not False)
print('True or not False : ', True or not False)

print('\nnot True and False : ', not True and False)
print('not True or False : ', not True or False)

print('\nnot True and not False : ', not True and not False)
print('not True or not False : ', not True or not False)

print('\nnot True : ', not True)
print('not False : ', not False)


    # If Statements ------------------------------------
print('\n -----------------IF STATEMENTS------------------- \n')

if True:
    print('True')
 
if False:
    print('False') # This will not be printed
    
x = 5
if x == 5:
    print('x is 5')
else:
    print('x is not 5') # This will not be printed
    
x = 0
if x == 5:
    print('x is 5') # This will not be printed
else:
    print('x is not 5')
    
for x in range (5):
    if x == 3:
        print('3 ! |', end=' ')
    else:
        print('no.. x is', x, '|', end=' ')


    # If Statements with Lists ------------------------------------
print('\n\n -----------------IF STATEMENTS WITH LISTS------------------- \n')

list = [1, 2, 3, 4, 5]
if 3 in list:
    print('3 is in list')
    
if 6 in list:
    print('6 is in list') # This will not be printed
else:
    print('6 is not in list')
    
if 6 not in list:
    print('6 is not in list')
    
if 3 not in list:
    print('3 is not in list') # This will not be printed
else:
    print('3 is in list')
    
    
    # If Statements with Strings ------------------------------------
print('\n -----------------IF STATEMENTS WITH STRINGS------------------- \n')

string = 'Hello World'

if 'Hello' in string:
    print('Hello is in string')
    
    
    # If Statements with Tuples ------------------------------------
print('\n -----------------IF STATEMENTS WITH TUPLES------------------- \n')

tuple = (1, 2, 3, 4, 5)

if 3 in tuple:
    print('3 is in tuple')
    

    # If Statements with Dictionaries ------------------------------------
print('\n -----------------IF STATEMENTS WITH DICTIONARIES------------------- \n')

dict = {'a': 1, 'b': 2, 'c': 3}

if 'a' in dict:
    print('a is in dict')
    
# value = dict['a'] or dict.values()

if 1 in dict.values():
    print('1 is in dict values')

if 1 in dict:
    print('1 is in dict') # This will not be printed
else:
    print('1 is not in dict')
    
    
    
    # Elif (else if) ------------------------------------
print('\n -----------------ELIF------------------- \n')

x = 5
if x == 5:
    print('x is 5')
elif x == 6:
    print('x is 6')
else:
    print('x is not 5 or 6')
    
    
    
    # Short Hand If ------------------------------------
print('\n -----------------SHORT HAND IF------------------- \n')

x = 6

if x == 5: print('x is 5')

#with else
print('x is 5') if x == 5 else print('x is not 5')

#with elif
print('x is 5') if x == 5 else print('x is 6') if x == 6 else print('x is not 5 or 6')
    
    
    
    # While Condition ------------------------------------
    
print('\n -----------------WHILE CONDITION------------------- \n')

x = 0
while x < 5:
    print(x, end=' ')
    x += 1 # x = x + 1
    
print('\n')


    # Break ------------------------------------   
print('\n -----------------BREAK------------------- \n')

x = 0
while True:
    print(x, end=' ')
    x += 1
    if x == 5:
        print('break !')
        break
    
    
    # Continue ------------------------------------
print('\n -----------------CONTINUE------------------- \n')

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue # Skip 3
    print(x, end=' ')
    
    
    # Else ------------------------------------