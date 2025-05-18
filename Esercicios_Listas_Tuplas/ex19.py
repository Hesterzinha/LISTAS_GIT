nomes = []

while True:
    nome = input('Digite um nome (ou "sair" para encerrar): ')
    if nome == '': 
        print('Nome vazio, tente novamente.')
        continue
    if nome.lower() == 'sair':  # lower() -> converte para minusculo
        break
    nomes.append(nome)
print(f'Nomes digitados: {nomes}')
