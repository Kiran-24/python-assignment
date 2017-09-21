# a) square of number b) area of triangle c) area of circle
# d) area of a rectangle.
from math import pi

def main():

	x = float(input('enter a number: '))
	#lambda for square of a number
	square = lambda x: x*x
	print(square(x))


	base = float(input('enter base of triangle: '))
	height = float(input('enter height of triangle: '))
	#lambda for area of triangle
	area_traingle = lambda base,height : base*height*0.5
	print(area_traingle(base,height))

	radius = float(input('enter radius of circle: '))
	#lambda for area of circle
	area_circle = lambda radius: pi * radius**2
	print(area_circle(radius))

	sidex = float(input('enter length of horizontal side: '))
	sidey = float(input('enter length of vertical side: '))
	#lambda for area of rectangle
	area_rectangle = lambda sidex,sidey : sidex*sidey
	print(area_rectangle(sidex,sidey))


if __name__ == '__main__':
	main()