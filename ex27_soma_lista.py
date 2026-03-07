lista = []

while True:
        n = input("Digite um número ou 'f'para encerrar:")
        if n == 'f':
            break
        lista.append(int(n))

        
print(f"Sua lista é {lista} e soma de todos os itens é {sum(lista)}.")
