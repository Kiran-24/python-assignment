'''Implement a python code to count 
	a) number of characters 
	b) number of words 
	c) number of lines 
from an input file to output file.'''

def num_characters(content):
	'''to count number of characters'''
	return len(content)

def num_words(content):
	'''to count number of words'''
	return len(content.split())

def num_lines(content):
	'''to count number of lines'''
	return len(content.split('\n'))

def main():
	f = open('demo.txt','r')
	content = f.read()
	f.close()
	char_count = num_characters(content)
	word_count = num_words(content)
	line_count = num_lines(content)
	f = open('count.txt','w')
	f.write('number of characters %d \n'%char_count)
	f.write('number of words %d \n'%word_count)
	f.write('number of lines %d \n'%line_count)
	f.close()

if __name__ == '__main__':
	main()