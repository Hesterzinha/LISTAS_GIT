lista = []

for numero in range(1, 6):
    numero = int(input('Digite um número: '))
    lista.append(numero)
lista.sort()
print(f'maior numero: {lista[4]}        | menor numero: {lista[0]}')

'''OU'''

for numero in range(1, 6):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    
max = max(lista)
min = min(lista)

print(f'maior numero: {max}        | menor numero: {min}')
