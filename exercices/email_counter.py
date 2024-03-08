# Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.

fname = input('File name: ')
fhost = open(fname)
counter = dict()

for line in fhost: 
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    words = line.split(' ')
    word = words[1]
    counter[word] = counter.get(word, 0) + 1

print(counter)