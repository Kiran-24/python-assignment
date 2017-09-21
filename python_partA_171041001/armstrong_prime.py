'''Implement a python code to check whether a given number is 
ARMSTRONG number or prime or both.'''

def is_armstrong(number):
	'''to check whether the given number is armstrong'''
	num_digits = len(str(number))
	sum = 0
	temp = number
	while temp > 0:
   		digit = temp % 10
   		sum += digit ** num_digits
   		temp //= 10
	if number == sum:
		return True
	else:
		return False

def is_prime(number):
	'''to check whether the given number is prime'''
	if number > 1:
		for i in range(2,(number//2)+1):
			if number % i == 0:
				return False
	return True

	
def main():
	number = int(input('enter a number: '))
	isArmstrong = is_armstrong(number)
	isPrime = is_prime(number)
	if isArmstrong:
		str_armstrong = 'ARMSTRONG'
	else:
		str_armstrong = 'not ARMSTRONG'

	if isPrime:
		str_prime = 'PRIME'
	else:
		str_prime = 'not PRIME'

	print('The given number is '+str_armstrong+' and is '+str_prime)


if __name__ == '__main__':
	main()