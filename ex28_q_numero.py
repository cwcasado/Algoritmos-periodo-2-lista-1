lista = [1,2,4,6,1,2,8,9,10,8]
contador = 0
numero = int(input("Digite um número para consultar : "))

for n in lista:
    if n == numero:
     contador = contador + 1


print(f'O número consultado foi {numero} e ele parece {contador} vezes na lista.')