
from os import system,remove
### to install tqdm in anaconda uncomment below lines ###
### tqdm is used for progress bar

# system('conda install -c conda-forge tqdm')

from tqdm import tqdm
import requests

def download(file,url):
	'''to download file from given url 
		and store in current directory'''
	# send get request
	data = requests.get(url, stream=True)
	# get size of file from header
	size = int(data.headers['Content-Length'])
	# write content to file
	for chunk in tqdm(data.iter_content(),total=size):
		file.write(chunk)

def main():
	url = 'https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.13.3.tar.xz'
	file_name = url.split('/')[-1]
	file = open(file_name,'wb')
	download(file,url)
	# delete downloaded file
	check = input("enter \'r\' to delete the doenloaded file: ")
	if check == 'r':
		remove(file_name)

if __name__ == '__main__':
	main()