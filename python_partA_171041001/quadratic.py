'''Implement a python code to solve quadratic equation'''

from cmath import sqrt            #for complex square root

def main():
	a = float(input('Enter the coefficient of x**2: '))
	b = float(input('Enter the coefficient of x: '))
	c = float(input('Enter the value of constant: '))

	discriminant = (b**2) - (4*a*c)
	root_one = (-b + sqrt(discriminant))/(2*a)
	root_two = (-b - sqrt(discriminant))/(2*a)
	print('the solutions are (%.2f%+.2fi) and (%.2f%+.2fi)' %(root_one.real,root_one.imag,root_two.real,root_two.imag))


if __name__ == '__main__':
	main()