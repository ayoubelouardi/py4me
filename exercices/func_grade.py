#   Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(s):
    if s >= 0.9 and s <= 1:
        return('A')
    elif s >= 0.8 and s < 0.9:
        return('B')
    elif s >= 0.7 and s < 0.8:
        return('C')
    elif s >= 0.6 and s < 0.7:
        return('D')
    elif s < 0.6 and s >= 0: 
        return('F')
    else:
        return('Bad score')

try:
    score = input('Enter score: ')
    s = float(score)
    
    print(computegrade(s))
except:
    print('Bad score')