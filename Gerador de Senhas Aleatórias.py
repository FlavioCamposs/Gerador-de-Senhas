import random
from time import sleep

print('-' * 40)
print('\033[1m{:^40}\033[m'.format('GERADOR DE SENHAS ALEATÓRIAS'))
print('-' * 40)

print('Seja muito bem vindo ao gerador de senhas aleatórias,\npreencha as informações que serão solicitadas a você: ')

print('-' * 59)

print('Só há apenas uma regra para gerar a sua senha:')
print('\033[1mSUA SENHA DEVERÁ TER NO MÁXIMO 8 CARACTERES!\033[m')
print()


while True:
    #PEDINDO AS INFORMAÇÕES
    letras = int(input('1° - Quantas letras você quer que tenha na senha?: '))
    #CONDIÇÃO APENAS PARA O PROGRAMA NÃO FAZER A PERGUNTA ABAIXO CASO O USUÁRIO NÃO QUEIRA NENHUMA LETRA
    if letras != 0:
        letrasMm = str(input('2° - Você deseja letras MAIUSCULAS ou minusculas? [M/m]: '))[0]
    numeros = int(input('3° - Quantos números você deseja?: '))
    simbolos = int(input('4° - Quantos símbolos?: '))

    while (letras + numeros + simbolos) <= 8:
        #GERANDO AS LETRAS E VERIFICANDO SE É "M" OU "m"
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        min = '' #aqui ele já irá receber a letra maiuscula ou minuscula
        letList = list()
        if letras != 0 and letrasMm == 'm':
            for c in range(1, letras+1):
                min = random.choice(abc)
                letList.append(min)
        elif letras != 0 and letrasMm == 'M':
            for c in range(1, letras+1):
                min = random.choice(abc).upper()
                letList.append(min)

        if letras == 0 and numeros == 0 and simbolos == 0:
            print('-' * 59)
            print('Dados inválidos!')
            break


        print('-' * 59)
        print('GERANDO SENHA...')
        sleep(2)
        print('-' * 59)

        #GERANDO OS NUMEROS
        nums = 0
        numList = list()
        if numeros != 0:
            n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for c in range(1, numeros+1):
                nums = random.choice(n)
                numList.append(nums)

        #GERANDO OS SÍMBOLOS
        s = ''
        simList = list()
        if simbolos != 0:
            simb = ['!', '?', '@', '#', '$', '%', '&', '*', '(', ')', '°', '<', '>', '/', '-', '+', '=', 'º', 'ª', ':', ';', '.', ',', '-', '_', '|', '[', ']', '{', '}', '§']
            for c in range(1, simbolos+1):
                s = random.choice(simb)
                simList.append(s)

        #JUNTANDO OS DADOS OBTIDOS
        senha = list()
        senhaOrganizada = list()

        #CASO TENHA TODOS OS DADOS
        if letras != 0 and numeros != 0 and simbolos != 0:
            senha.append(letList) #letras
            senha.append(numList) #numeros
            senha.append(simList) #simbolos
            for c in senha[0]:
                senhaOrganizada.append(c)
            for i in senha[1]:
                senhaOrganizada.append(i)
            for a in senha[2]:
                senhaOrganizada.append(a)

        #CASO TENHA APENAS 2 DADOS
        elif simbolos == 0:
            senha.append(letList)
            senha.append(numList)
            for c in senha[0]:
                senhaOrganizada.append(c)
            for i in senha[1]:
                senhaOrganizada.append(i)
        elif numeros == 0:
            senha.append(letList)
            senha.append(simList)
            for c in senha[0]:
                senhaOrganizada.append(c)
            for i in senha[1]:
                senhaOrganizada.append(i)
        elif letras == 0:
            senha.append(numList)
            senha.append(simList)
            for c in senha[0]:
                senhaOrganizada.append(c)
            for i in senha[1]:
                senhaOrganizada.append(i)

        #CASO TENHA APENAS 1 DADO
        elif letras == 0 and numeros == 0:
            senhaOrganizada.append(simList)
        elif letras == 0 and simbolos == 0:
            senhaOrganizada.append(numList)
        elif numeros == 0 and simbolos == 0:
            senhaOrganizada.append(letList)

        random.shuffle(senhaOrganizada)

        print('SENHA GERADA!')
        print('A senha é: ', end='')
        for c in senhaOrganizada:
            print(c, end='')
        print()
        pc = str(input('Deseja gerar outra senha? [S/N]: ')).upper()[0]
        if pc == 'N':
            print('-' * 59)
            print('Muito obrigado e até a próxima!')
            break
    else:
        print('VOCÊ EXCEDEU O LIMITE DE CARACTERES!')
    break