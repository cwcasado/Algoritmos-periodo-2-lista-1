numeros = []

while True:
    n = input("Digite um número ou 'f' para encerrar:")

    if n == 'f':
        break
    numeros.append(int(n))
lista_unica = list(dict.fromkeys(numeros))
print(f'Sua primeira lista é {numeros} e sua lista sem duplicatas é essa {lista_unica}.')
