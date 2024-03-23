import urllib.request, re

url = input("Enter - ")

fhand = urllib.request.urlopen(url)

count = 0
for line in fhand:
    line = line.decode().strip()
    count += len(line)
    if count <= 3000:
        print(line)
    else:
        for a, b in line, range(3000):
            print(a, end='')

# http://data.pr4e.org/romeo.txt