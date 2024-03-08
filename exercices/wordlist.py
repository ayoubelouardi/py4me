# Write a program that reads the words in words.txt and stores them
# as keys in a dictionary. It doesn't matter what the values are. Then 
# you can use the in operator as a fast way to check whether a string is
# in the dictionary.

words = {}

fname = input('File name: ')
try:
    fhost = open(fname)
except:
    print('Invalid value')
    exit()

count = 1
for word in fhost:
    word = word.rstrip("\n")
    if word in words: continue
    words[word] = count
    count += 1

for x in range(len(words)):
    print(words[x])