#! python3
 # bulletPointAdder.py - Adds Wikipedia bullet points to the start
 # of each line of text on the clipboard.
import pyperclip
listName = pyperclip.paste()
names=listName.split('\n')
for i in range(len(names)):
    names[i]='*'+names[i]
pyperclip.copy('\n'.join(names))
