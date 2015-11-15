#Jonas Vanden Branden

def is_palindrome(string):
	size = len(string)
	half = int(len(string)//2)
	for i in range(0,half):
		if(string[i] != string[size-i-1]):
			return False

	return True

def largest():
	num1 = 999
	num2 = 999
	turn1 = True
	found=False
	while(found==False and num1>99 and num2>99):
		if(turn1):
			num1-=1
		else:
			num2-=1
		turn1=not turn1
		num=num1*num2
		print(num)
		if(is_palindrome(str(num))):
			found=True
			return num

if __name__ == "__main__":
	print(largest())
