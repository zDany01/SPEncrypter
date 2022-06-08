from os import path, remove as deleteDir, system as execute
from time import sleep
from platform import system
from cryptography.fernet import Fernet

def generateKey(regenerate):
    if regenerate: deleteDir("key")
    open("key","w").write(Fernet.generate_key().decode())
    print("New key generated.")


def main():
    if not path.exists("key"):
        generateKey(False)
        exit()
    else: key = open("key","r").read().encode()

    fernet = Fernet(key)

    reply = input("1. Encrypt\n2. Decrypt\n3. Generate New Key\n\nChoose: ")
    if reply == "1":
        print(fernet.encrypt(input("Write text to encrypt: ").encode()).decode())
    elif reply == "2":
        try: print(fernet.decrypt(input("Write encrypted text: ").encode()).decode())
        except: print("Key doesn't match.\nUnable to decrypt.")
    elif reply == "3":
        print("By generating a new key, you will lose the ability do decrypt all previously encrypted text\nDo you wish to continue? [y/N]")
        if(input().upper().split()[0]) == 'Y': key = generateKey(True)
        else: print("Aborting...")
        sleep(1)
        if system() == "Windows": execute("cls")
        else: execute("clear")
        main()



if __name__ == "__main__": main()