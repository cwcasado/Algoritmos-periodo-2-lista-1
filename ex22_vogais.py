texto = input("Digite uma palavra:")
n_vogais = 0
vogais = "aeiou"

for letra in texto.lower():
    if letra in vogais:
        n_vogais += 1

print(f"O texto tem {n_vogais} vogais.")
