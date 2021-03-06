'''
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


class KriMath:
    '''
    pokec
    '''

    def __init__(self, number):
        self.number = number

    def factor(self):
        factors = []
        for i in range(1, int(self.number ** (1 / 2)) + 1):
            if self.number % i == 0:
                factors.append(i)
        return factors

    def factorCount(self):
        count = len(self.factor())
        return count


'''
cislo = 600851475143
pocetDelitelov = 0
delitele = []
max_delitel = []
for i in range(1, int(cislo ** (1/2)) + 1):
    if cislo % i == 0:
        delitele.append(i)
        pocetDelitelov = pocetDelitelov + 1

for i in delitele:
    if ((2 ** i) - 2) % i == 0:
        max_delitel = [i]

print("pocet delitelov: ", pocetDelitelov)
print("delitele: ", delitele)
print("max. prvociselny delitel: ", max_delitel)
'''
