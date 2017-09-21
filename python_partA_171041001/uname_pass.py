''' Implement a python code to get the username and password.'''

from getpass import getpass

def main():
	dictionary={}
	uname = input('enter the username:')
	dictionary[uname] = getpass()
	print('username: ' + uname +'\npassword: '+ dictionary[uname])


if __name__ == '__main__':
	main()