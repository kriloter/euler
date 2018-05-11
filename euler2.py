# https://projecteuler.net/problem=2

fibo_start = [1, 2]
fibo_even = []
fibo = 0
temp = 0

while temp < 4000000:
    fibo = fibo_start[-2] + fibo_start[-1]
    fibo_start.append(fibo)
    temp = fibo_start[-1]
fibo_start = fibo_start[:-1]

for i in fibo_start:
    if i % 2 == 0:
        fibo_even.append(i)

print("\n", "komplet fibo: \n", fibo_start, "\n", "suma: ", sum(fibo_start))
print("\n", "parne fibo: \n", fibo_even, "\n", "suma: ", sum(fibo_even))
