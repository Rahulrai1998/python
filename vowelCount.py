def vowelCount(str):
	count = 0
	vowels = ['a' , 'e' , 'i' , 'o' , 'u']
	for i in str:
		if i in vowels:
			count+=1
	return count 

if __name__ == "__main__":
	
	str = input("Input the string  = ")
	res = vowelCount(str)
	print(f"{str} has {res} vowels and {len(str)-res} consonants . ")
	