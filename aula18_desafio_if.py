valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1 > valor2:
    print(f'Valor {valor1} é maior que {valor2}')
elif valor1 == valor2:
    print("Os números são iguais")
else:
    print(f'Valor {valor2} é maior que {valor1}')