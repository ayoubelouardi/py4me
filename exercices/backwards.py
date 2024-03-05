#   Write a while loop that starts at the last character in the string 
# and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

string = input('Enter a string: ')
index = len(string)

while index > 0:
    print(string[index - 1])
    index = index - 1