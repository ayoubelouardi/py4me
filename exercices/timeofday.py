# This program counts the distribution of the hour of the day for each 
# of the messages. You can pull the hour from the "From" line by finding 
# the time string and then splitting that string into parts using the colon
# character. Once you have accumulated the counts for each hour, print out 
# the counts, one per line, sorted by hour.

fname = input('File name: ')
try: 
    fhost = open(fname)
except:
    print('The file does\'t exist!')
    exit()

counter = dict()

for line in fhost:
    if not line.startswith('From'): continue 
    if line.startswith('From:'): continue
    #
    words = line.split(' ')

    word = words[6]
    #
    words = word.split(':')
    word = words[0]
    #
    counter[word] = counter.get(word, 0) + 1

#    
tmp = list(counter.items())

tmp.sort()
for tuple in tmp:
    print(tuple[0], tuple[1])