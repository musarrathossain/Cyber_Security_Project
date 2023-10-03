import socket
import tkinter as tk
from cryptography.fernet import Fernet
import pyperclip


def generate_key():
    return Fernet.generate_key()


def send_message():
    message = message_entry.get()
    receiver_ip = receiver_ip_entry.get()
    receiver_port = int(receiver_port_entry.get())
    receiver_address = (receiver_ip, receiver_port)

    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())

    print("Sending encrypted message:", encrypted_message)

    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender.sendto(encrypted_message, receiver_address)
    sender.close()
    print("Message sent.")


def set_key():
    global key
    key = generate_key()
    key_label.config(text=f"Generated Key: {key.decode()}")
    print("Generated key:", key.decode())


def copy_key_to_clipboard():
    pyperclip.copy(key.decode())
    print("Key copied to clipboard:", key.decode())


key = generate_key()

root = tk.Tk()
root.title("Sender - Secret Texting Tool")

key_label = tk.Label(root, text=f"Generated Key: {key.decode()}")
key_label.pack()

copy_key_button = tk.Button(root, text="Copy Key to Clipboard", command=copy_key_to_clipboard)
copy_key_button.pack()

message_label = tk.Label(root, text="Enter your message:")
message_label.pack()

message_entry = tk.Entry(root, width=40)
message_entry.pack()

receiver_ip_label = tk.Label(root, text="Receiver's IP address:")
receiver_ip_label.pack()

receiver_ip_entry = tk.Entry(root, width=15)
receiver_ip_entry.pack()

receiver_port_label = tk.Label(root, text="Receiver's port:")
receiver_port_label.pack()

receiver_port_entry = tk.Entry(root, width=8)
receiver_port_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

set_key_button = tk.Button(root, text="Set New Key", command=set_key)
set_key_button.pack()

root.mainloop()
