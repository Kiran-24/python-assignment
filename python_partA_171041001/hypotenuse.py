''' implement a python code to find the hypotenuse of a right angle triangle.'''

from math import sqrt

def main():
	adjacent = float(input('enter length of adjacent side: '))
	opposite = float(input('enter length of opposite side: '))
	hypotenuse = sqrt(adjacent**2 + opposite**2)
	print('the length of hypotenuse is %.2f' %hypotenuse)


if __name__ == '__main__':
	main()