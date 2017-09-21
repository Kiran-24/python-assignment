import struct
'''pack returns string according to given format
	h - short int size: 2 bytes
	@ - native system format
	< - little endian format
	> - big ensian format'''

def endian():	
	native = struct.pack('@h', 1)
	print('\nnative: {0}'.format(native))
	little_endian = struct.pack('<h', 1)
	print('little endian: {0}'.format(little_endian))
	big_endian = struct.pack('>h', 1)
	print('big endian: {0}'.format(big_endian))
	if endian:
		print('\nsystem is LIITLE ENDIAN\n')
	else:
		print('\nsystem is BIG ENDIAN\n')

def main():
	endian()

if __name__ == '__main__':
	main()