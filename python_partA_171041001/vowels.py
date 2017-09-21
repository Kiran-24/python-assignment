''' implement a python code to check to a) count total number of vowels b) individual count of
vowel characters'''

vowels = 'aeiou'

string = input('enter the string: ')
string.lower()

#dictionary to store individual count of vowels
vowel_count = {}.fromkeys(vowels,0) 

#counting individual vowels
for char in string:
	if char in vowels:
		vowel_count[char] +=1

print('individual count of vowels is ',vowel_count)

print('The total count of vowels is ',sum(vowel_count.values()))