import zmq
import random
import sys
import time
import json

port = "5556"
list_test=[1,2,3,"test","testing",3.5,'afdshkjsadfkjslkdfj;']
#list_test=json.dumps(list_test)
dict_test={'first':'124','second':'456','third':list_test}
dict_test=json.dumps(dict_test)
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
#socket.bind("tcp://localhost:%s" %port)

while True:
    #socket.send("Server message to client3")
    socket.send(dict_test)
    msg = socket.recv()
    print msg
    time.sleep(1)

