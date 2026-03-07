numeros = []
while True:
 n = input("Digite um número ou digite 'fim' para encerrar:")
 if n == 'fim':
  break
 
 numeros.append(int(n))
 
numeros.sort()
print(numeros)


