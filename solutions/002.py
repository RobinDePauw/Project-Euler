#Jonas Vanden Branden
def even_fib(x):
	even_sum = 0
	fib1 = 1
	fib2 = 1
	while(fib2 < x):
		if(fib2%2==0):
			even_sum+=fib2
		temp = fib1 + fib2
		fib1 = fib2
		fib2 = temp
	return even_sum


if __name__ == "__main__":
	print (even_fib(4000000))