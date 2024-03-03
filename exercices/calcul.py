#   Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.

count = 0
total = 0
average = 0

while True:
    num = input('Enter a number: ')
    try:
        num = int(num)
        count = count + 1
        total = num + total
        average = total / count
    except:
        if num == 'done':
            print(total, count, average) # print the result
            break
        else:
            print('Invalid input')
            continue
