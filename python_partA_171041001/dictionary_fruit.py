'''Create a dictionary of a) fruit name and its number B) Create a list from the dictionary for
only orange and apple.'''

def main():
	fruits_dict = {'banana': 6, 'apple': 3, 'orange': 2, 'pear': 5}
	# creating list of form [[fruit,number],[fruit, number]]
	fruits_list = [[key,fruits_dict[key]] for key in ('orange','apple')]
	print(fruits_list)


if __name__ == '__main__':
	main()