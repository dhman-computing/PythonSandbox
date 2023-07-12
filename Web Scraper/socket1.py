import socket
# import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# print(cmd)
mysock.send(cmd)

## Time test
# print("Going to sleep......")
# time.sleep(10)
# print("Waking up......")

data = ''
while True:
    _ = mysock.recv(512).decode()
    if len(_) < 1:
        break
    data += _
    # print(data)
    # print(data.decode(), end='')

print(data, end='')

## Writing the response in a file
# with open('data_socket1.txt', 'w') as file:
#     file.write(data)
    

mysock.close()
