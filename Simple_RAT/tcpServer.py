import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0',9999))

s.listen()

conn, addr = s.accept()

#print('Connection: ' + str(conn))
print('Connection Recieved From: ' + addr[0])

while True:
	command = input('CMD> ')

	if command == 'exit':
		conn.send('exit'.encode('utf-8'))
		conn.close()
		break

	conn.send(command.encode('utf-8'))
	print(conn.recv(4096).decode('utf-8'))
