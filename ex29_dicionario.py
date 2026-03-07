dicionario = {}

while True:
    nome = input("Digite o nome (ou 'f' para sair): ")
    if nome.lower() == 'f':
        break
        
    idade = input("Digite a idade (ou 'f' para sair): ")
    if idade.lower() == 'f':
        break
    
    dicionario[nome] = int(idade)
    
    print(f"Cadastrado com sucesso! Estado atual: {dicionario}")

print(f"\nLista final de cadastros: {dicionario}")
