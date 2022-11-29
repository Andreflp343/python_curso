num = input('Digite um número inteiro: ')

try:
    num_int = float(num)

    num_par_impar = num_int % 2 == 0

    if num_par_impar:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('Digite um número inteiro')
