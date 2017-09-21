'''implement a python code to find the area of a triangle.'''

from math import sqrt

def area(a,b,c):
	''' to find the area of triangle'''
	#inequality theorem
	if a+b>c and b+c>a and c+a>b:			
		#semi-perimeter of triangle
		s = (a+b+c)/2	
		#Heron's formula to find area of trinagle				
		area_of_triangle = sqrt(s*(s-a)*(s-b)*(s-c))  	 
		print('Area of given triangle is %.2f' %area_of_triangle)
	else:
		print('sum of two sides must be greater than third')


def main():
	a = float(input('enter the length of side one: '))
	b = float(input('enter the length of side two: '))
	c = float(input('enter the length of side three: '))
	area(a,b,c);
	

if __name__ == '__main__':
	main()