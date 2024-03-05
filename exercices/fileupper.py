#   Write a program to read through a file and print the
# contents of the file (line by line) all in upper case. 

fname = input('Enter the name of the file: ')
fhandle = open(fname)

for line in fhandle: 
    print(line.upper(), end="")
print('') # for the new line in the end