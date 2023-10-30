from tkinter import *
from pathlib import Path
import json
from time import sleep
import random

root = Tk()
root.title("Pick a Winner")
root.iconbitmap("static/logo-icon.ico")
root.geometry("300x300")

entries = json.loads(Path("points.json").read_text())

labelText = StringVar()
labelText.set("Pick the Winner")

fontName = "Shabnam"

# cheat = 'who_to_win_username'
cheat = False

exclude_users = ['instagram', 'messi']

def Pick():
    global root, entries, labelText, winButton, cheat

    winButton['state'] = 'disabled'
    root.update()
    
    entries_set = []
    for entry in entries:
        if entry in exclude_users:
            continue
        for i in range(0, entries[entry]):
            entries_set.append(entry)
    
    random.shuffle(entries_set)

    rando = random.randint(0, len(entries_set) - 1)
    total_entries = len(entries)

    counter = 1
    for i in entries:
        counter += 1
        labelText.set(i)
        root.update()
        percent = (counter / total_entries) * 100
        sleep(percent / 1000)
    
    if cheat:
        labelText.set(cheat)
    else:
        labelText.set(entries_set[rando])
    winButton['state'] = 'active'
    root.update()

topLabel = Label(root, text="Pick the Winner", textvariable=labelText, font=(fontName, 16))
topLabel.pack(pady=50)

winButton = Button(root, text="Pick the WINNER!!", font=(fontName, 14), command=Pick)
winButton.pack(pady=25)

root.mainloop()