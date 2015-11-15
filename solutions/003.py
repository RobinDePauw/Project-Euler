#Jonas Vanden Branden
def is_prime(x):
	half = int(x//2)
	for i in range(2,half):
		if(x%i==0):
			return False
	return True

def largest(x,y):
	if(x>y):
		return x
	else:
		return y

def largest_prime(x):
	if(is_prime(x)):
		return x
	else:
		found = False
		divider = 2
		while(found==False):
			if(x%divider==0):
				found = True
				return largest(divider,largest_prime(int(x//divider)))
			if(divider>x):
				print("Error")
				found = True
			divider+=1
 

if __name__ == "__main__":
	print(largest_prime(600851475143))
