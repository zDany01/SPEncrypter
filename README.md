# SPEncrypter
This is a simple python text encrypter program that work using [Fernet](https://cryptography.io/en/latest/fernet/).

The program will generate a key file on the first start that will be used for encrypting and decrypting text.  
If for some reason, __the key is damaged or lost__, the program will not be able to decrypt anymore the text that has been encrypted before using that key.  
⚠️ **So a backup for the "key" file present in the folder is raccomanded** ⚠️

## How to setup
1. [Download](https://github.com/zDany01/SPEncrypter/releases) or clone the repository
2. install the requirements:
  >pip install -r requirements.txt
3. Run the program for the first time to generate the key
  >python3 SPEncrypter.py  
  
 ![key](https://user-images.githubusercontent.com/85403430/141861344-eeb43892-7a25-4f2c-8b01-ff7dda44bd92.png)

<br>
     
 
 ### How to use the program
 Run the program
 >python3 SPEncrypter.py

 Select 1 if you want to encrypt text  
![crypt](https://user-images.githubusercontent.com/85403430/141862646-f5eb1675-95b1-481d-a3ae-b6b7b8b23dea.png)
 Select 2 if you want to decrypt text
![decrypt](https://user-images.githubusercontent.com/85403430/141862370-e244581f-b205-4441-81a0-b0174ba71f78.png)
 Enter text to encrypt or decrypt
 ![result](https://user-images.githubusercontent.com/85403430/141862653-bd50be00-4527-4178-ba16-1116fc6779ca.png)

#### Additional Info
if you want to change the key, you can delete the current key and the program will generate a new one or you can change in the python file the NewKey variable
![code](https://user-images.githubusercontent.com/85403430/141863053-1696f5e1-9732-4bb7-8e11-4bc5d26ab7cf.png)
