nome = 'André'

tamanho_nome = len(nome)

nova_string = ''

i = 0

while i < tamanho_nome:

    nova_string += '*' + nome[i] + '*'
    print(nova_string)
    i += 1


