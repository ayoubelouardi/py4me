import socket

url = input("Enter - ")
host = url.split('/')
try:
    if host[1] == []: print("Processing...")
    if host[0] == "https:" or host[0] == "http:": print("")
except:
    print("Error - Not a valid URL")
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host[2], 80))
# replacing this with the url
past = 'GET '+ url +' HTTP/1.0\r\n\r\n'
cmd = past.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# Code: http://www.py4e.com/code3/socket1.py
# Or select Download from this trinket's left-hand menu