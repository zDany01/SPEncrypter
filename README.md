# SPEncrypter
This is a simple python text encrypter program that works using [Fernet](https://cryptography.io/en/latest/fernet/).

On the first run, the program will generate a key file that will be used for encrypting and decrypting text.  
If for some reason, __the key is damaged or lost__, the program will __not__ be able to decrypt previously encrypted text which used that key.  
⚠️ **So a backup for the encryption key is recommended** ⚠️

<details>
  <summary>Rapid Links</summary>
  <ul>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#how-to-use-the-program">How to use the program</a>
        <ul>
        <li><a href="#encrypt-text">Encrypt Text</a></li>
        <li><a href="#decrypt-text">Decrypt Text</a></li>
        <li><a href="#generate-a-new-key">Generate a new Key</a></li>
        </ul>
    </li>
  </ul>
</details>


## Setup
1. [Download](https://github.com/zDany01/SPEncrypter/releases) the latest version or clone the repository
2. Install the requirements
```sh
pip install -r requirements.txt
```
6. Generate the key by running the program for the first time
```sh
python SPEncrypter.py
```
 ![GenerateKey](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/GenerateKey.png?raw=true)


<br>

## How to use the program
First, start up the program
```sh
python SPEncrypter.py
```

### Encrypt text
>Select 1 to enter encryption mode 
![EncryptMenu](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/EncryptionMode.png?raw=true)

Enter the text that you want to encrypt, for example, `Hello, World!`, and press enter

![EncryptedText](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/EncryptedText.png?raw=true)

<br>

### Decrypt text
>Select 2 to enter decryption mode 
![DecryptMenu](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/DecryptionMode.png?raw=true)

Enter encrypted text, in this case `gAAAAABioQmfkrueSLiHVLWuQeslv-K3ad5T4C2VFqgS_Yo9W-yjBcGzjx66Tp97nei1OJzjjhh3fvxgDVEw01YBsUgkMsIrWQ==`, and press enter
![EncryptedText](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/DecryptedText.png?raw=true)

<br>



### Generate a new Key

**WARNING**
If you replace your current key, all the text that you have previously encrypted using your old key will become undecryptable

>Select 3 to generate a new Key
![GeneratorMenu](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/GeneratorMenu.png?raw=true)

Type `Y` to confirm
![ConfirmKey](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/ConfirmKey.png?raw=true)
![SuccessKey](https://github.com/zDany01/zDany01/blob/main/Assets/SPEncrypter/SuccessKey.png?raw=true)