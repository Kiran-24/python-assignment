import sys
import argparse
import re

def count(fp):
	''' return number of time/s Embedded is found
	in input file'''
	search_obj = re.findall(r'Embedded',fp.read())
	return len(search_obj)

def main():
	parser = argparse.ArgumentParser(description='Hello World')
	parser.add_argument('-d',help='display on console',action = 'store_true')
	parser.add_argument('file_input',help='input file name')
	parser.add_argument('file_output',help='Output file name')
	args = parser.parse_args()
	input_file = args.file_input
	output_file = args.file_output
	try:
		input_fp = open(input_file,'r')
		cnt = count(input_fp)

		output_fp = open(output_file,'w')
		msg = 'number of times \'Embedded\' found in '+ input_file +' file is: ' + str(cnt)
		output_fp.write(msg)
	except IOError as e:
		print('I/O error: {0}'.format(e))
	
	if args.d:
		print(msg)

if __name__ == '__main__':
	main()