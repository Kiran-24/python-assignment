'''Implement a python code to find the height of a tree from distance x
Assumptions: 1.The entered distance and height are assumed to be in feet
			 2. angle_elevation in degrees '''

from math import tan
from math import radians

def height_tree(distance,height_observer,angle_elevation):
	''' To calculate height of tree 
		given: distance of tree from observer
			   height of observer
			   and angle of elevation'''
	return tan(radians(angle_elevation)) * distance + height_observer

def main():
	distance = float(input('enter the distance of tree from observer :'))
	height_observer = float(input('enter the height of observer: '))
	angle_elevation = float(input('enter the angle of elevation: '))

	height = height_tree(distance,height_observer,angle_elevation)

	print('the height of tree is %.2f' %height)


if __name__ == '__main__':
		main()