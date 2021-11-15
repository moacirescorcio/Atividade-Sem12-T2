n = int(input())
ultimo = 0
penultimo = 1
for c in range(n+1):
    proximo = ultimo + penultimo
    penultimo = ultimo
    ultimo = proximo

print(ultimo, penultimo, proximo)
