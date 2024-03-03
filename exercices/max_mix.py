#   Write another program that prompts for a list of numbers 
# as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

max = None
min = None

while True:
    num = input('Enter a number: ')
    try:
        num = int(num)
        if max is None or max <= num:
            max = num
        elif min is None or min >= num:
            min = num
    except:
        if num == 'done':
            print('Maximum is', max) # print the result
            print('Minimum is', min)
            break
        else:
            print('Invalid input')
            continue