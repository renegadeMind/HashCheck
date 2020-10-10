#This little script allows you to check SHA-256 checksums easily by just running the script
#in the format >>>pyhton checkSHA256.py [-k] [-f]
#[-k] is the SHA-256 checksum provided by the download provider.
#[-f] is the path to the downloaded file. With MacOS you can just drag the file over the terminal app.

import sys, hashlib

providedHash = sys.argv[1]
fileLocation = sys.argv[2]
fileHash = None
BLOCK_SIZE = 65536

#Header
print('\x1b[97;1;49m***********************\n'
	+ '*                     *\n' 
	+ '*      \x1b[32;1;49mHashCheck\x1b[97;1;49m      *\n'
	+ '*                     *\n'
	+ '***********************\x1b[0m\n')

#Disclaimer
print('\x1b[93;1;49m Disclaimer: Opening any file on the basis of the results of this software is at the risk of the user. We do not take any responsibility.\x1b[0m\n\n\n')

#Asking the user what kind of hashfunction he would like to test against
print('What encryption Method has been used?')
print('[1] MD5     [3] SHA-256')
print('[2] SHA-1   [4] Exit')
input = input('Input: ')
print('\n')

#MD5 decission-tree
if input == '1' or input == 'MD5' or input == 'md5':
	print('\x1b[91;3;49m MD5 is proven to be unsafe. We recommend that you use SHA-256 if available.\x1b[0m')

	fileHash = hashlib.md5()
	with open(fileLocation, 'rb') as file:
		file_block = file.read(BLOCK_SIZE)
		while len(file_block) > 0:
			fileHash.update(file_block)
			file_block = file.read(BLOCK_SIZE)
	fileHash = fileHash.hexdigest()
	if providedHash== fileHash:
		print('\x1b[32;3;49m Both hashes match.\x1b[0m Because the MD5 hash-function has been used, only open the file if you trust the site you downloaded the file from.')
	else:
		print('\x1b[91;3;49m The hashes do not match! We recommend that you delete the file immediately.\x1b[0m')

#SHA-1 decission-tree
elif input == '2' or input == 'SHA-1' or input == 'sha-1' or input == 'SHA1' or input == 'sha1':
	print('\x1b[91;3;49m SHA-1 is proven to be unsafe. It is recommended that you use SHA-256 if available.\x1b[0m')
	
	fileHash = hashlib.sha1()
	with open(fileLocation, 'rb') as file:
		file_block = file.read(BLOCK_SIZE)
		while len(file_block) > 0:
			fileHash.update(file_block)
			file_block = file.read(BLOCK_SIZE)
	fileHash = fileHash.hexdigest()

	#Check if both hashes match
	if providedHash == fileHash:
		print('\x1b[32;3;49m Both hashes match.\x1b[0m Because the SHA-1 hash-function has beeen used, only open the file if you trust the site you downloaded the file from.')
	else:
		print('\x1b[91;3;49m The hashes do not match! We recommend that you delete the file immediately.\x1b[0m')
#SHA-256 decission-tree
elif input == '3' or input == 'SHA-256' or input == 'sha-256' or input == 'SHA256' or input == 'sha256':

	fileHash = hashlib.sha256()
	with open(fileLocation, 'rb') as file:
		file_block = file.read(BLOCK_SIZE)
		while len(file_block) > 0:
			fileHash.update(file_block)
			file_block = file.read(BLOCK_SIZE)
	fileHash = fileHash.hexdigest()

	if providedHash == fileHash:
		print('\x1b[32;3;49m Both SHA-256 hashes are the same. You should be safe to open the file.\x1b[0m')
	else:
		print('\x1b[91;3;49m The SHA-256 hashes do not match! We recommend deleting the file immediately.\x1b[0m')

else:
	print('\n\nWe hope we could help you keep your computer safe.')
	sys.exit()

print('\n\nWe hope we could help you keep your computer safe.')
sys.exit()
