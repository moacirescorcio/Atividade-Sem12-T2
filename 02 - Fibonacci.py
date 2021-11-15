anterior = 0
proximo = 0
lista = []
n = int(input())

for c in range(n):
    lista.append(proximo)    
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1

print(*lista, sep=", ")