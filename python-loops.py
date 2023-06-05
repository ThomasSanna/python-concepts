# Python loops tutorial

    # For loop ------------------------------------
    
print('\n -----------------FOR LOOP------------------- \n')

for x in range(10): # range(10) means 0 to 9
    print(x, ' ', end="") # end="" means no new line
    
print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
for object in grocery_list:
    print(object, end=" ")
    
print('\n ------------------------------------ \n')
    
for x in [2,4,6,8,10]:
    print(x, end=" ")
    
print('\n ------------------------------------ \n')

for x in [2,4,6,8,10]:  
    print(x-1, end=" ")
    
print('\n ------------------------------------ \n')

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y], end=" ")
    print('\n')
    


    # While loop ------------------------------------
print('\n -----------------WHILE LOOP------------------- \n')


import random
    
random_num = random.randrange(0,100)
while(random_num != 15):
    random_num = random.randrange(0,100)
    print(random_num, end=" ")
    
print('\n ------------------------------------ \n')

i = 0
while(i <= 20):
    if(i%2 == 0):
        print(i, end=" ")
    elif(i == 9):
        print('i hate 9')
    i += 1
    
print('\n ------------------------------------ \n')

while True and False:
    print('True and False') # this will never print
    break

while True and True:
    print('True and True') # this will print forever
    break # this will stop the loop

print('\n ------------------------------------ \n')

while True or False:
    print('True or False') # this will print forever
    break

while False or False:
    print('False or False') # this will never print
    break # this will stop the loop