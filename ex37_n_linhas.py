import os

nome_arquivo = r"coloque seu texto aqui"

if os.path.exists(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        total = sum(1 for linha in arquivo)
        print(f"O arquivo tem {total} linhas.")
else:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    print(f"Arquivos na pasta atual: {os.listdir()}")

