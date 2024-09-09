#!/usr/bin/python3.9
import sys
import pyperclip
PASSWORDS = {'college-id':'f@pilani'
             ,'library-id':'hello123'
             ,'myname':'coolpass123'}

if len(sys.argv) < 2:
    print ('hey you need to provide the username as the command line argument for which u want the password')
else:
    id = sys.argv[1]
    password = PASSWORDS[id]
pyperclip.copy(password)

