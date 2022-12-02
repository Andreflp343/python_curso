nome = 'André'

tamanho_nome = len(nome)

nova_string = ''

i = 0

while i < tamanho_nome:

    nova_string += f'*{nome[i]}'
    i += 1

nova_string += f'*'
print(nova_string)
