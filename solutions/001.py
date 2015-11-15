#Jonas Vanden Branden

def find_sum_below(x):
	lists = list_multiples_below(3,x)+list_multiples_below(5,x)
	lists.sort()
	answer =  0
	print(lists)
	mem=0
	for i in lists:
		if (i==mem):
			continue
		answer +=i		
		mem=i

	return answer

def list_multiples_below(base,x):
	mult_list = []
	var = base
	while (var<x):
		mult_list.append(var)
		var +=base
	return mult_list

if __name__ == "__main__":
	print (find_sum_below(1000))