# Write a program that categorizes each mail message by which
# day of the week the commit was done. To do this look for lines
# that start with "From", then look for the third word and keep a
# running count of each of the days of the week. At the end of the
# program print out the contents of your dictionary (order does not matter).

fname = input('File name: ')
fhost = open(fname)
counter = dict()

for line in fhost:
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue # we shoud remove 'From:' lines
    words = line.split(' ')
    word = words[2]
    counter[word] = counter.get(word, 0) + 1

print(counter)