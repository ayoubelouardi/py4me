# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(word, alpha):
    n = 0
    for letter in word:
        if letter == alpha:
            n = n + 1
    return n

    
word = input('Give me the word: ')
c = input('Give me the character: ')

print(count(word, c))