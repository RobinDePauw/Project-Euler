import time
"""
11
5
1
3
2
6
7
8
9
10
57
99
"""
__author__ = 'ROBIN'

# Straight forward methode
# n = int(input())
# for _ in range(n):
#     c = int(input())
#     sumC = 0
#     for x in range(1,c+1):
#         sumC = sumC + x**3
#     print(str(sumC))

# Betere methode
n = int(input())
for i in range(n):
    c = int(input())
    print(str(int((c**2)*(c+1)**2/4)))

