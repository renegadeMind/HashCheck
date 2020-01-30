#This little script allows you to check SHA-256 checksums easily by just running the script
#in the format >>>pyhton checkSHA256.py [-k] [-f]
#[-k] is the SHA-256 checksum provided by the download provider.
#[-f] is the path to the downloaded file. With MacOS you can just drag the file over the terminal app.

import subprocess, sys, platform

providedHash = sys.argv[1]
fileLocation = sys.argv[2]
platform = platform.system()
fileHash = None

#Header
print('\x1b[97;1;49m***********************\n'
	+ '*                     *\n' 
	+ '*      \x1b[32;1;49mHashCheck\x1b[97;1;49m      *\n'
	+ '*                     *\n'
	+ '***********************\x1b[0m\n')

#Disclaimer
print('\x1b[93;1;49m Disclaimer: Any installations made on the basis of the result of this software are at the risk of the end-user.\x1b[0m\n\n\n')

#If the users operating system is not supported the script informs the user and terminates.
if platform != 'Windows' and platform != 'Darwin':
	print('Your operating system is not supported by this script.')
	sys.exit()

#Asking the user what kind of hashfunction he would like to test against
print('What encryption Method has been used?')
print('[1] MD5     [3] SHA-256')
print('[2] SHA-1')
input = input('Input: ')

#MD5 decission-tree
if input == '1' or input == 'MD5' or input == 'md5':
	print('\x1b[91;3;49m MD5 is proven to be unsafe. We recommend that you use SHA-256 if available.\x1b[0m')
	if platform == 'Windows':
		fileHash = subprocess.check_output('FCIV -md5 ' + fileLocation, shell=True)

	elif platform == 'Darwin':
		fileHash = subprocess.check_output('md5 ' + fileLocation, shell=True)
		#cutting the output to md5.length+1 because the string ends with \n
		fileHash = fileHash[-33:]
		#removing the \n at the end of the string
		fileHash = fileHash[:32]

	if providedHash.encode('utf-8') == fileHash:
		print('Both hashes match. Because the MD5 hash-function has been used, only open the file if you trust the site you downloaded the file from.')
	else:
		print('\x1b[91;3;49m The hashes do not match! We recommend that you delete the file immediately.\x1b[0m')
#SHA-1 decission-tree
elif input == '2' or input == 'SHA-1' or input == 'sha-1' or input == 'SHA1' or input == 'sha1':
	print('\x1b[91;3;49m SHA-1 is proven to be unsafe. It is recommended that you use SHA-256 if available.\x1b[0m')
	if platform == 'Windows':
		fileHash = subprocess.check_output('FCIV -sha1 ' + fileLocation, shell=True)

	elif platform == 'Darwin':
		fileHash = subprocess.check_output('shasum -a 1 ' + fileLocation, shell=True)
		#Get the first 40 characters of the output string
		fileHash = fileHash[:40]
	#Check if both hashes match
	if providedHash.encode('utf-8') == fileHash:
		print('Both hashes match: Because the SHA-1 hash-function has beeen used, only open the file if you trust the site you downloaded the file from.')
	else:
		print('\x1b[91;3;49m The hashes do not match! We recommend that you delete the file immediately.\x1b[0m')
#SHA-256 decission-tree
else:
	#Here we calculate the SHA checksum for the provided file
	if platform == 'Windows':
		fileHash = subprocess.check_output('certutil -hashfile ' + fileLocation + ' SHA256', shell=True)
	elif platform == 'Darwin':
		fileHash = subprocess.check_output('shasum -a 256 ' + fileLocation, shell=True)
		#Get the first 64 characters of the output
		fileHash = fileHash[:64]

	if providedHash.encode('utf-8') == fileHash:
		print('Both SHA-256 hashes are the same. You should be safe to install the software.')
	else:
		print('\x1b[91;3;49m The SHA-256 hashes do not match! We recommend deleting the file immediately.\x1b[0m')
#orderly exitting the program
sys.exit()
