palavra = input("Digite uma palavra:")

if palavra == palavra[::-1]:
    print("Essa palavra é um palíndromo.")

else:
    print("Essa palavra não é um palíndromo.")