__author__ = 'ROBIN'
"""
Pizzabonnen
http://www.vlaamseprogrammeerwedstrijd.be/2015/opgaven/cat3/pizzabonnen/pizzabonnen.pdf
"""
def free_pizza_per_bon(bon):
    if bon[0] == 0:
        return 100000.
    else:
        return float(bon[1])/float(bon[0])

def freePriceAdvantage(bon,pizzas):
    if bon[0] == 0:
        return 100000.
    elif bon[1] ==0:
        return 0
    else:
        total = sum(pizzas[:bon[0]+bon[1]])
        pay = sum(pizzas[:bon[0]])
        free = sum(pizzas[bon[0]:bon[0]+bon[1]])
        return total/bon[0] - free/bon[1]

def cheapest(s_bonnen,s_pizzas,prijs):
    if s_pizzas is None or len(s_pizzas) == 0:
        return prijs
    elif s_bonnen is None or len(s_bonnen) == 0:
        return prijs+sum(s_pizzas)
    s_bonnen.sort(key=lambda x: (-free_pizza_per_bon(x),-freePriceAdvantage(x,s_pizzas)))

    bon = s_bonnen.pop(0)
    if bon[0] >= len(s_pizzas):
        return cheapest(s_bonnen,s_pizzas,prijs)
    elif bon[0] + bon[1] > len(s_pizzas):
        nieuwe_bon = tuple([bon[0],bon[1]-1])
        s_bonnen.append(nieuwe_bon)
        return cheapest(s_bonnen,s_pizzas,prijs)
    else:
        prijs += sum(s_pizzas[:bon[0]])
        s_pizzas = s_pizzas[bon[0]+bon[1]:]
        return cheapest(s_bonnen,s_pizzas,prijs)

def main():
    n = int(input())
    for i in range(n):
        pizzas = input()
        pizzas = list(pizzas.split())
        pizzas = pizzas[1:]
        pizzas = list(map(int,pizzas))
        pizzas.sort(reverse=True)
        m = int(input())
        bonnen = list()
        for j in range(m):
            bon = tuple(map(int,input().split()))
            bonnen.append(bon)
        bonnen.sort(key=lambda x: (-free_pizza_per_bon(x),-freePriceAdvantage(x,pizzas)))
        print(str(i+1)+" "+str(cheapest(bonnen,pizzas,0)))


main()
