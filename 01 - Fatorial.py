n = int(input('Insira um número: '))
resultado = 1
lista = []
for c in range(1, n+1):
    lista.append(c)    
    
for numero in lista:
    resultado *= numero

print(f'O fatorial desse número é {resultado}')
