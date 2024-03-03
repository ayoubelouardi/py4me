#   Write a program which prompts the user for a Celsius temperature, 
# ... convert the temperature to Fahrenheit, and print out the converted temperature.

# the formila = (C * 9/5) + 32 = F

celsius = input('Celsius: ')
c = float(celsius)

f = (c * 9/5) + 32

print('Fahrenheit:', f)