"""
3
3
23
42
13
2
100
97
1
42
"""
n_lists = int(input())
for i_list in range(1,n_lists+1):
    n_numbers = int(input())
    max = min = int(input())
    for i_number in range(n_numbers-1):
        number = int(input())
        if number > max:
            max = number
        elif number < min:
            min = number
    print("{0!s} {1!s} {2!s}".format(i_list,min,max))
