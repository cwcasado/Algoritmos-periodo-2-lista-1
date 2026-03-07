def fatorial(n):
    if n < 0: 
        return "Só números inteiros podem ser fatorados."
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

n = int(input("Digite um número para fatoração :"))

print(f"Resultado {fatorial(n)}.")  
