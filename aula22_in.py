#nome = 'André'
#print(nome [2])
#print(nome [-1])

#print('d' not in nome)
#print('dré' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digte o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
