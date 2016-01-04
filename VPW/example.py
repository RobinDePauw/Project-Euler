__author__ = 'ROBIN'
"""
INPUT:
4
4 programmeren
13 implementatie
3 winnen
1 team
"""

letters = int(input())
for _ in range(letters):
    positie, woord = input().rstrip().split()
    print(woord[int(positie) - 1])