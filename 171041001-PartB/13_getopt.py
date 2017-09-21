import sys
import getopt
import re

def count(fp):
	''' return number of time/s Embedded if found
	in input file'''
	search_obj = re.findall(r'Embedded',fp.read(),flags=re.IGNORECASE)
	return len(search_obj)

def main():
	opts, args = getopt.getopt(sys.argv[1:],'h',['help='])
	if opts and opts[0][0] in ('-h','--help'):
		print('01_getopt.py <inputfile> <outputfile>')
		sys.exit()
	if len(args) == 2:
		input_file = args[0]
		output_file = args[1]
	else:
		print('usage: 01_getopt.py <inputfile> <outputfile>')
		sys.exit()
	
	try:
		input_fp = open(input_file,'r')
		cnt = count(input_fp)

		output_fp = open(output_file,'w')
		msg = 'number of times \'Embedded\' found in '+ input_file +' file is: ' + str(cnt)
		output_fp.write(msg)
	except IOError as e:
		print('I/O error: {0}'.format(e))

if __name__ == '__main__':
	main()