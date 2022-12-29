import random
def numeros_para_mega():
    lista = []
    while len(lista) < 6:
        x = random.randint(1,60)
        if x not in lista:
            lista.append(x)
    return(lista)


print(numeros_para_mega())
