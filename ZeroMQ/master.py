# coding: utf8
import socket  
import zmq

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(("", 8080))                                    
sock.listen(5)  
while True:                                          
	conn, addr = sock.accept()                                
	print("we got connection from", addr)

	request = conn.recv(1024).decode()
	print 'Request is ', request

	f = request.split('GET /')[1].split(' HTTP')[0]
	print 'File is ', f

	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	port = "5555"
	socket.connect ("tcp://localhost:%s" % port)

	socket.send_string(f)
	message = socket.recv()
	print "Received reply ", message

	if message == 'Not found' :
	   mes = '<html><head><title>404 Error</title></head><body><p>Not Found!</p></body><html>'
	   response = 'HTTP/1.1 404 Not Found\r\nContent-Length: ' + str(len(mes)) + '\r\n\r\n'+mes
	   conn.send(response.encode())
	else : 
	   l = len(message)
	   response = 'HTTP/1.1 200 OK\r\nContent-Length: ' + str(l) + '\r\n\r\n'+message
	   conn.send(response.encode())

conn.close()

