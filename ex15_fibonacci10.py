def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Imprimir os primeiros 10 números
fibonacci(10)
# Saída: 0 1 1 2 3 5 8 13 21 34
