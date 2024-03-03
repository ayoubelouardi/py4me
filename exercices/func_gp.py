#   Rewrite your pay computation with time-and-a-half for overtime and create a function called 
# computepay which takes two parameters (hours and rate).
def computepay(houre, rate):
    
    if houre > 40:
        return (40 * rate) + ((houre - 40) * (1.5 * rate))
    else:
        return houre * rate


try:
    hours = input('Enter Hours: ')
    hrs = float(hours)
    rate = input('Enter Rate: ')
    r = float(rate)

    pay = computepay(hrs, r)

    print('Pay:', pay)
except: 
    print('Error, please enter numeric input')