# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input('Enter Hours: ')
hrs = float(hours)
rate = input('Enter Rate: ')
r = float(rate)
pay = r * hrs

print('Pay:', pay)