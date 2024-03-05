# Rewrite the program that prompts the user for a list of numbers and prints
# out the maximum and minimum of the numbers at the end when the user enters
# "done". Write the program to store the numbers the user enters in a list and
# use the max() and min() functions to compute the maximum and minimum numbers
# after the loop completes.

alist = []

while True: 
    n = input('Enter a number: ')
    try: 
        n = int(n)
        alist.append(n)
    except:
        if n == 'done': 
            print('Maximum:', max(alist))
            print('Minimum:', min(alist))
            exit()
        print('Invalid value')


