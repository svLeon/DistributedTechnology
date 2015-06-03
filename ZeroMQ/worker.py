# coding: utf8
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
port = "5555"
socket.bind("tcp://*:%s" % port)

def readFile(name) :
   try :
   	file = open(name, "r")
   	l = file.readline()
   	s = ''
   	while(len(l) > 1):
   	   s = s + l
   	   l = file.readline()
   except IOError as e :
        s = 'Not found'
   finally :
        return s

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message # add not found
    responce = readFile(message)
    socket.send_string(responce)
