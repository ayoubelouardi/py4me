# Add code to the above program to figure out who has the
# most messages in the file.

# give me a list and i will return the index of the bigest value
def bindex(alist):
    for i in alist: 
        if alist[i] == max(alist): 
            return i

fname = input('File name: ')
fhost = open(fname)
counter = dict()

for line in fhost: 
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue 
    words = line.split(' ')
    word = words[1]
    counter[word] = counter.get(word, 0) + 1

vlist = counter.values() # creat a list of the dict value 

for key in counter: 
    if max(vlist) == counter[key]:
        print(key, max(vlist))