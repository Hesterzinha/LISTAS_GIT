lista = []

for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número: '))
    lista.append(numero)
    if numero % 2 == 0:
        lista.remove(numero)

print(f'A lista final é: {lista}')
