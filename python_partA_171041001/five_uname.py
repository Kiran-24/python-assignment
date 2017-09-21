''' Implement a python code to get 5 username and password and store it in dictionary'''

from getpass import getpass

def main():
	dictionary = {}
	x=0
	while x<5 :
		username = input('enter the username of %d: ' %x)
		if username in dictionary.keys():
			print('username already exists')
			continue
		dictionary[username] = getpass()
		x+=1	
	print(dictionary)

if __name__ == '__main__':
	main()