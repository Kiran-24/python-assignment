''' Implement a python code to find the centroid of a triangle'''

def centroid(p1,p2,p3):
	''' To calculate the centroid of triangle'''
	centroid = [(p1[0]+p2[0]+p3[0])/3 , (p1[1]+p2[1]+p3[1])/3]
	return centroid

def main():
	print('enter x y co-ordinates of first vertex :')
	p1 = [float(d) for d in input().split()]

	print('enter x y co-ordinates of second vertex :')
	p2 = [float(d) for d in input().split()]

	print('enter x y co-ordinates of third vertex :')
	p3 = [float(d) for d in input().split()]

	x_y = centroid(p1,p2,p3)
	print('the centroid of triangle is (%.2f , %.2f)' %(x_y[0],x_y[1]))

if __name__ == '__main__':
	main()