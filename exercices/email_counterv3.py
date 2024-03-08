# Revise a previous program as follows: Read and parse the "From" lines and pull
# out the addresses from the line. Count the number of messages from each person 
# using a dictionary.

# After all the data has been read, print the person with the most commits by creating 
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse 
# order and print out the person who has the most commits.

counter = dict()

fname = input('File name: ')
try:
    fhost = open(fname)
except:
    print('File does\'t exict!')
    exit()


for line in fhost: 
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    words = line.split(' ')
    word = words[1]
    counter[word] = counter.get(word, 0) + 1

tmp = list(counter.items()) # creat a list of the dict value 

t = list() # revers of tmp

for x, y in tmp:
    t.append((y,x))

t.sort(reverse=True) 

num, email = t[0]

print(email, num)