# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter
# frequency varies between languages.

import string


fname = input('File name: ')
try: 
    fhost = open(fname)
except:
    print('the file doesn\'t excit!')
    exit()

alphacounter = dict()

for line in fhost:
    line = line.translate(str.maketrans('','',string.punctuation + string.digits))
    #
    line = line.lower()
    #
    for alpha in line: 
        if alpha == ' ' or alpha == '\n' or alpha == '\t': continue
        alphacounter[alpha] = alphacounter.get(alpha, 0) + 1

tmp = list(alphacounter.items())
tmp.sort()

t = list()

for a, b in tmp:
    t.append((b ,a))

t.sort(reverse=True)


for da in range(len(t)):
    print(t[da],'|',tmp[da])