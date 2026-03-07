valores = []
while True:
    n = input("Digite um número ou 'fim' para encerrar: ")
    if n == 'fim':
        break
    valores.append(n)
    print(f"O maior valor é {max(valores)} e o menor é {min(valores)}")
