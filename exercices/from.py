# Write a program to read through the mail box data and when you find
# line that starts with "From", you will split the line into words using 
# the split function. We are interested in who sent the message, which is 
# the second word on the From line.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for 
# each From line, then you will also count the number of From
# (not From:) lines and print out a count at the end.

def extractit(alist):
    return alist[1] # return the second word in the list

thelist = []
count = 0

fname = input('File name: ')
try: 
    fhost = open(fname)
except:
    print('the file does\'t exist')
    exit()

for line in fhost:
    if not line.startswith('From'): continue
    word = extractit(line.split(' '))
    if word[-1] == '\n':
        word = word[:-1] # remove every \n from the emails
    thelist.append(word)
    count += 1

for x in range(len(thelist)):
    print(thelist[x])
print('There were', count,'lines in the file with From as the first word')