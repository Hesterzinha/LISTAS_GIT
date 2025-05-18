lista = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero > 10:
        lista.append(numero)
        print(f'O número {numero} é maior que 10.')
    elif numero < 10:
        lista.append(numero)
        print(f'O número {numero} é menor que 10.')
    else:
        lista.append(numero)
        print(f'O número {numero} é igual a 10.')

print(f'A lista final é: {lista}')
