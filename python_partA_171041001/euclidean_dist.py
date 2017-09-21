'''Implement a python code to find the distance between two points.(Euclidean distance)'''

from math import sqrt

def euclidian_dist(p1: list,p2: list):
	'''to find distance between two point'''
	return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def main():
	print('enter x y co-ordinates of first point :')
	p1 = [float(d) for d in input().split()]

	print('enter x y co-ordinates of second point :')
	p2 = [float(d) for d in input().split()]

	distance = euclidian_dist(p1,p2)
	print('distance between two points is %.2f' %distance)



if __name__ == '__main__':
	main()