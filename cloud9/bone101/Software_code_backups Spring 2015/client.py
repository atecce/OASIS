import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.10.6:5000")

while True:
    socket.send("this is client")
    msg = socket.recv()
    print "Client received:", msg
    time.sleep(1)
