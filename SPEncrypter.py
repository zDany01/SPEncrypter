from os import path
from cryptography.fernet import Fernet
NewKey = False #set to true for generate a new key(All previous encrypted message will be undecryptable)
if not path.exists("key"): NewKey = True
if NewKey:
    key = Fernet.generate_key()
    open("key","w").write(key.decode())
    print("New key generated.")
    exit()
else: key = open("key","r").read().encode()
fernet = Fernet(key)
if input("1. Encrypt\n2. Decrypt\n") == "1":
    print(fernet.encrypt(input("Write text to encrypt: ").encode()).decode())
else:
    try:
        print(fernet.decrypt(input("Write encrypted text: ").encode()).decode())
    except:
        print("Key doesn't match.\nUnable to decrypt.")