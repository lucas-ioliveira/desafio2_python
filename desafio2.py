'''
1- Faça um programa que peça ao usuário para digitar um n´mero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um
número inteiro, informe que não é inteiro.
'''
# Solução 1
num_int = input('Digite um número inteiro: ')

if num_int.isdigit():
    num_int = int(num_int)

    if num_int % 2 == 0:
        print(f'{num_int} é par.')
    else:
        print(f'{num_int} é ímpar.')
else:
    print(f'Isso não é um número inteiro.')

'''
2- Faça um programa que pergunte a hora ao usuário e, baseando-se no
horário descrito, exiba a saudação apropriada.
'''
# Solução 2
horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario <0 or horario > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0 e 23.')


'''
3- Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4
letras ou menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "seu nome é normal"; maior que 6 escreva "seu nome é muito grande".
'''
#Solução 3
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'{nome} é um nome curto.')
elif tamanho <= 6:
    print(f'{nome} é um nome normal.')
else:
    print(print(f'{nome} é um nome grande.'))


