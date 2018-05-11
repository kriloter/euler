# https://projecteuler.net/problem=1

sucet = 0
for cislo in range(1, 100):
    if cislo % 3 == 0 or cislo % 5 == 0:
        sucet = sucet + cislo
print("\n", sucet)
