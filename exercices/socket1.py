import urllib.request

url = input("Enter - ")

try:
    fhand = urllib.request.urlopen(url)
    count = 0 
    total = 0
    for line in fhand:
        line = line.decode().strip()
        for l in line:
            total += 1
            if total <= 3000:
                print(l, end='')
                count += 1
    print("\n")
    print("I printed :", count, "letters", "of", total)
except:
    print("Error - Not a valid URL")
    exit()

# Code: http://www.py4e.com/code3/socket1.py
# Or select Download from this trinket's left-hand menu