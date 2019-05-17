from argparse import ArgumentParser
from os import path,rename
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


#Encryption of files
def encrypt(filename,key):
	key=getKey(key)
	chunksize =64 * 1024
	outputFile =filename+'.enc'
	filesize = str(path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk +=b' ' * (16-(len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))

#Decryption of files
def decrypt(filename,key):
	key=getKey(key)
	chunksize =64 * 1024
	outputFile = filename[:-4]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
				outfile.truncate(filesize)

def getKey(password):
	if password is None:
		password="MyDefaultPassword"
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()


parser = ArgumentParser()
parser.add_argument('-e','--encrypt-file', help='Encrypt a given file', required=False)
parser.add_argument('-p','--password', help='Password used for encryption and decryption', required=False)
parser.add_argument('-d','--decrypt-file', help='Decrypt a given file', required=False)

args = parser.parse_args()

if args.encrypt_file:
	print('encrypting=',args.encrypt_file)
	encrypt(args.encrypt_file,args.password)
	print('Done!')
elif args.decrypt_file:
	print('decrypting=',args.decrypt_file)
	decrypt(args.decrypt_file,args.password)
	print('Done!')
else:
    parser.print_help()
 
