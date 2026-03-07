a = float(input("Digite o primeiro número :"))
b = float(input("Digite o segundo número :"))
c = float(input("Digite o terceiro número :"))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

print(f"O maior número é {maior} .")