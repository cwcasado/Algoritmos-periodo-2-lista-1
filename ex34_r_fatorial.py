def fatorial(n):
    if n <= 1:
        return 1

    else:
        return n * fatorial(n - 1)

n_fat = int(input('Digite o valor a ser fatorado: '))
fat = fatorial(n_fat)

print(fat)