# FileEncrypter

This program is used for encrypting and decrypting files using AES 256-bit key encryption.

A user-defined password can also be defined for secure encryption and decryption.
All given passwords are converted to a 256-bit key using [SHA256 Hash Algorithm](https://en.bitcoinwiki.org/wiki/SHA-256).
Since hash for any two given passwords can never be the same, 256-bit key generated is also unique, thus the confidentiality of the encrypted file is guaranteed.

## Installation

Download the [FileEncrypter.py](https://github.com/bharavi15/FileEncrypter/blob/master/FileEncrypter.py) file.

## Usage

### Display help information

`python FileEncrypter.py
`
### Encryption and Decryption of file using the default password
Encryption- `python FileEncrypter.py -e filename.txt`

Decryption-`python FileEncrypter.py -d filename.txt.enc`


### Encryption and Decryption of file using a user-defined password
Encryption- `python FileEncrypter.py -e filename.txt -p MyPassword`


Decryption-`python FileEncrypter.py -d filename.txt.enc -p MyPassword`

**Note-** Encrypted file is saved as `filename.txt.enc`
