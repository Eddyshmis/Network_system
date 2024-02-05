import tkinter as tk
import customtkinter
import system_control as sys_c
from time import sleep


root = customtkinter.CTk()
root.geometry("500x200")





master = sys_c.Main_system()

user_input = customtkinter.StringVar()
user_input.set("")

def connect_comps():
    master.start_server()

def close_listen_fun():
    master.server.close()

def shut_computers_fun():
    master.gui_msg = "shutdown /s"
    sleep(0.001)
    master.gui_msg = ""

def send_message():
    master.gui_msg = user_input.get()
    #need better system other than wait a bit till the system gets it thats stupid
    sleep(0.1)
    master.gui_msg = ""





Connection_frame = customtkinter.CTkFrame(root)
Connection_frame.grid(row=0,column=0)

connect_btn = customtkinter.CTkButton(Connection_frame, text= "Connect",command= connect_comps )
connect_btn.grid(row=0, column=0,padx=10)

close_listen_btn = customtkinter.CTkButton(Connection_frame, text="Close listen",command=close_listen_fun)
close_listen_btn.grid(row=0, column=1,padx=10)

shut_computers_btn = customtkinter.CTkButton(Connection_frame, text="System_shutdown",command=shut_computers_fun)
shut_computers_btn.grid(row=0, column=2,padx=10,pady=20)

text_input = customtkinter.CTkEntry(Connection_frame,textvariable=user_input,width= 50)
text_input.grid(row=1,column=0)

submit_btn = customtkinter.CTkButton(Connection_frame, text="Submit",command= send_message)
submit_btn.grid(row=2,column=0)



root.mainloop()