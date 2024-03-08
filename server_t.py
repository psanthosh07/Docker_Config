import socket
s=socket.socket()
port=1000
s.bind(('',port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from ",port)
    a=c.recv(1024)
    m=a.upper()
    print(m)
    c.send(bytes(m,'utf-8'))
