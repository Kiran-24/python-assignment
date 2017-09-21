
#print the kernel version of system
from platform import system, release

def main():
	print('This system has {0} kernel of version {1}'.format(system(),release()))

if __name__ == '__main__':
	main()