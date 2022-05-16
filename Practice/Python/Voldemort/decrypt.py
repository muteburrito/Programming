import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file =="mykey.key" or file == "decrypt.py" or file == "decrypt.exe" or file == "voldemort.exe" :
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("mykey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as myfiles:
        contents = myfiles.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)

    with open(file, "wb") as myfiles:
        myfiles.write(contents_decrypted)

print("Files decrypted successfully !!")
exit = input("Press any key continue..")