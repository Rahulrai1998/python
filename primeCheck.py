def primeCheck(n):
	flag = True
	for i in range(2 , int(n/2)+1):
		if n%i==0 :
			flag = False
			break
	return flag

if __name__ == "__main__" :
	n = int(input("Enter the number to check = "))
	res = primeCheck(n)
	if res:
		print("Prime Number")
	else:
		print("Not Prime") 
		
	