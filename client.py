import random
import socket
import time
from threading import Thread
from tkinter import *

sock = socket.socket()

sock.connect(('zebaro24.tplinkdns.com', 25565))

root = Tk()

root.title("zeite")
root.geometry("500x600")

text = Text(root)
text.insert(END, "\n"*25)

text.pack()
entry = Entry(width=50, xscrollcommand=True)
entry.pack()
def add_message(message):
    text.config(state="normal")
    text.insert(END, f"{message}")
    text.config(state="disabled")
    text.see(END)


def send(message):
    sock.send(message.encode("UTF-8"))
def recieve():
    while True:
        data = sock.recv(1024).decode('UTF-8')
        if data:
            print(f"{data}")
            add_message("\nden: ")
            add_message(data)
def get_message():
    message = entry.get()
    entry.delete(0,END)
    send(message)
    add_message(f"\ndima: {message}")

def get_message_bind(key):
    get_message()
Thread(target=recieve).start()

btn_send= Button(text="send", command=get_message)
btn_send.pack()



root.bind("<Return>", get_message_bind)
root.mainloop()
