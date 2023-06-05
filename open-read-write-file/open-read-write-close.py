    # open(), read(), write(), close()	Opens, reads, writes and closes files-------------------------------

print('\n------open-------')

#in the terminal, cd to the folder where the file is located (cd python-concepts/built-in-functions)

file = open('test.txt', 'w') # w = write mode (other modes : r = read, a = append)
file.write('Hello World!')
file.close() # don't forget to close the file !

#writing in append mode
file = open('test.txt', 'a') # a = append mode
file.write(' [1, 2, 3, 4]')
file.write('\n [5, 6, 7, 8]')
file.close() 

#reading
file = open('test.txt', 'r')
print(file.read()) # print the whole file
file.close()

#reading line by line
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

print('\n------rstrip-------')

#reading with loop and removing \n
file = open('test.txt', 'r')
for line in file:
    print(line.rstrip())
file.close()

print('\n------split-------')

#reading with splitting
file = open('test.txt', 'r')
for line in file:
    print(line.split())
file.close()

print('\n------split with loop-------')