n = int(input("Digite um número: "))

if n > 1:
    print(f'{n} é um número primo.')
elif n % n == 0:
    print(f'{n} é um número primo.')
elif n == 2:
    print(f'{n} é um número primo.')
elif n % 2 == 0:
    print(f'{n} não é um número primo.')

else:
    print(f'{n} não é um número primo.')