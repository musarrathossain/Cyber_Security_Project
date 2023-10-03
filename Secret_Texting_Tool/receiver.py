import socket
import tkinter as tk
from cryptography.fernet import Fernet

def set_key():
    global key
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())
    messages_list.insert(tk.END, "Generated key. Enter this key in sender.")
    print("Generated key:", key.decode())

def receive_message():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind(('0.0.0.0', receiver_port))

    cipher_suite = Fernet(key)

    while True:
        encrypted_message, sender_address = receiver.recvfrom(4096)
        decrypted_message = cipher_suite.decrypt(encrypted_message)
        messages_list.insert(tk.END, f"From {sender_address[0]}: {decrypted_message.decode()}")
        print("Received encrypted message:", encrypted_message)
        print("Decrypted message:", decrypted_message.decode())

key = None

root = tk.Tk()
root.title("Receiver - Secret Texting Tool")

key_label = tk.Label(root, text="Enter the shared key or generate a new key:")
key_label.pack()

key_entry = tk.Entry(root, width=40)
key_entry.pack()

set_key_button = tk.Button(root, text="Generate New Key", command=set_key)
set_key_button.pack()

messages_list = tk.Listbox(root, width=40, height=10)
messages_list.pack()

receiver_port = 10000  # Use the same port as in sender_gui.py

receive_message_button = tk.Button(root, text="Start Receiving Messages", command=receive_message)
receive_message_button.pack()

root.mainloop()
