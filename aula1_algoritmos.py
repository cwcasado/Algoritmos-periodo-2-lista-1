def soma(a,b): 
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def testeAB():
    # global a
    # global b

    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: ")) 
 
    if a > b:
        print("certo")
    else:
        while(a<b):
            print("deu erro")
            a = float(input("Insira o primeiro valor: "))
            b = float(input("Insira o segundo valor: "))
            # print(a,b)

    return a,b
                
v1,v2 = testeAB()
# print(resultado)
resultado1 = soma(v1,v2)
resultado2 = subtracao(v1,v2)
resultado3 = multiplicacao(v1,v2)
resultado4 = divisao(v1,v2)

# print(resultado)
# print(f"{resultado1:.3f}")

print(f"Valores utilizados {v1} e {v2} ,soma = {resultado1:.3f}, subtração = {resultado2:.3f}, multiplicação = {resultado3:.3f}, divisão = {resultado4:.3f}")

