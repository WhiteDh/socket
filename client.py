import socket
from threading import Thread
import tkinter as tk

root = tk.Tk()
root.title("Text Input and Display")
with open("chat_history.txt", "r") as f:
    text = f.read()
    f.close()

text_field = tk.Text(root, height=10, width=30)
text_field.insert(tk.END, text+"\n")
text_field.pack()

entry = tk.Entry(root)
entry.pack()
def add_text_from_button():
    text = entry.get()
    text_field.insert(tk.END,"you: " + text + "\n")
    entry.delete(0, tk.END)
    send_message(text)

    messages = text_field.get("1.0", "end")
    save_chat(messages)
def add_text_recieved(text):
    text_field.insert(tk.END, text + "\n")

def on_enter_press(event):
    add_text_from_button()

root.bind('<Return>', on_enter_press)
button = tk.Button(root, text="Add", command=add_text_from_button)
button.pack()



def send_message(message):
    client_socket.sendall(message.encode('utf-8'))

def receive_message():
    while True:
        data = client_socket.recv(1024)
        if data:
            print("Received data:", data.decode('utf-8'))
            add_text_recieved(f"man: {data.decode('utf-8')}")
def save_chat(text):
    with open("chat_history.txt", "w") as f:
        f.write(text)
        f.close()
port = 12345
host = "localhost"
server_address = (host, port)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(server_address)

# Start send and receive threads
receive_thread = Thread(target=receive_message)
receive_thread.start()







root.mainloop()


# Wait for threads to finish
receive_thread.join()

# Close the socket
client_socket.close()
