import socket
import threading
import customtkinter
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

    def new_window_client(self,conn,addr):
        def close_client(conn):
            self.Connections -= 1
            self.new_window.destroy()
            conn.close()

        self.new_window = customtkinter.CTkToplevel()
        self.new_window.title(f"Connection {self.Connections}: {addr}")
        self.new_window.geometry("500x300")

        self.output_box = customtkinter.CTkTextbox(master= self.new_window,width=500,height=300)
        self.output_box.grid(column = 0, row = 0)
        self.output_box.insert(customtkinter.END,text="Client Started")

        close_btn = customtkinter.CTkButton(self.new_window,text="close",command=lambda:close_client(conn))
        close_btn.grid(column = 0, row = 1)

    
    def handle_client(self,conn,addr):
        self.connected = True
        self.server.setblocking(False)

        self.new_window_client(conn,addr)
        
        while self.connected:
            client_msg = conn.recv(2048).decode(self.FORMAT)
            if client_msg == "!Connected":
                try:
                    conn.send(str.encode("WORKS!",encoding=self.FORMAT))
                    break
                except Exception as e:
                    print("Error:",e)
        while self.connected:
            if client_msg != None:
                self.output_box.insert(customtkinter.END,text=f"\n{client_msg}")
                # print(client_msg)
            try:
                conn.send(str.encode(self.gui_msg,encoding=self.FORMAT))
                try:
                    client_msg = conn.recv(2048).decode(self.FORMAT)
                except:
                    client_msg = None
            except WindowsError as e:
                print("Error: ", e)
                break
            except Exception as e:
                print("Error:",e)
        self.Connections -= 1
        self.new_window.destroy()
        conn.close()
            




    def start_server(self):
        self.server.listen()

        
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        print(self.SERVER)

        def multiple_listening():
            while True:
                try:
                    conn, addr = self.server.accept()
                    
                    print("connected to: ", addr)
                    self.Connections += 1
                    thread = threading.Thread(target=self.handle_client,args=(conn,addr))
                    thread.start()
                    print(f"[ACTIVE CONNECTIONS]{self.Connections}")

                    
                    #get output box
                except BlockingIOError:
                    pass

        start_listening_thread = threading.Thread(target=multiple_listening)
        start_listening_thread.start()
        