!#/usr/bin/python3.9
import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i]='*' + lines[i]
asterisktext = '\n'.join(lines)
pyperclip(asterisktext)

