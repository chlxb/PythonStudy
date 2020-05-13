import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    # c.send(String) 会报错 需要对字符串encode 或者使用另外一种方法 bytes(msg, 'UTF8')
    msg = 'Thank you for conneting\n'
    c.send(msg.encode())
    c.send(bytes("I'm socket server", 'UTF8'))
    c.close()