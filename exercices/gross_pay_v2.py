#   Rewrite your pay computation to give the employee 1.5 times the hourly
# rate for hours worked above 40 hours.

#   Rewrite your pay program using try and except so that your program handles non-numeric
# input gracefully by printing a message and exiting the program. 

try:
    hours = input('Enter Hours: ')
    hrs = float(hours)
    rate = input('Enter Rate: ')
    r = float(rate)

    if hrs > 40:
        pay = (40 * r) + ((hrs - 40) * (1.5 * r))
    else:
        pay = hrs * r

    print('Pay:', pay)
except: 
    print('Error, please enter numeric input')