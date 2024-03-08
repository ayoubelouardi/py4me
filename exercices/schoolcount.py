# This program records the domain name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

fname = input('File name: ')
fhost = open(fname)
counter = dict()

for line in fhost:
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    words = line.split('@')
    words = words[1].split(' ')
    word = words[0]
    counter[word] = counter.get(word, 0) + 1

print(counter)