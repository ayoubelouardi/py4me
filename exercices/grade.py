#   Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error message. If the score is between 0.0 and 1.0, print a grade

score = input('Enter score: ')
s = float(score)

try:
    if s >= 0.9 and s <= 1:
        print('A')
    elif s >= 0.8 and s < 0.9:
        print('B')
    elif s >= 0.7 and s < 0.8:
        print('C')
    elif s >= 0.6 and s < 0.7:
        print('D')
    elif s < 0.6 and s >= 0: 
        print('F')
    else:
        print('Bad score')
except:
    print('Bad score')