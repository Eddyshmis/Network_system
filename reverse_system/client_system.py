import socket
import threading

class Main_system:
    def __init__(self):
        self.HEADER = 2084
        self.PORT = 5555
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.current_ship_pos = None

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.setblocking(True)
        self.Connections = 0
        self.gui_msg = ""
    
    def handle_client(self,conn,addr):
        connected = True
        while connected:
            client_msg = conn.recv(2048).decode(self.FORMAT)
            if client_msg == "!Connected":
                try:
                    conn.send(str.encode("WORKS!",encoding=self.FORMAT))
                    break
                except Exception as e:
                    print("Error:",e)
        while connected:
            try:
                conn.send(str.encode(self.gui_msg,encoding=self.FORMAT))
            except WindowsError as e:
                print("Error: ", e)
                break
            except Exception as e:
                print("Error:",e)
            




    def start_server(self):
        self.server.listen()
        
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        print(self.SERVER)

        def multiple_listening():
            while True:
                conn, addr = self.server.accept()
                
                print("connected to: ", addr)
                self.Connections += 1
                thread = threading.Thread(target=self.handle_client,args=(conn,addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS]{self.Connections}")

        start_listening_thread = threading.Thread(target=multiple_listening)
        start_listening_thread.start()
        