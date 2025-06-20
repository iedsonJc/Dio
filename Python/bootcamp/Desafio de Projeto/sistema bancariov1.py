#Desafio: Criando um Sistema Bancário
print(F'\033[2:31m{"BANCO DIO":^40}\033[m')
print('-=-'*20)

saldo = 0
numSaques = 1
limSaques = 3
limite = 500
tentSaques = 0
extra = ''

menu =""">>Menu de Operações<<:
      [1]Deposita
      [2]Sacar
      [3]Extrato
      [4]Sair
Escolha-> """

nome = str(input('Nome: ')).upper()
print(f"""Seja bem vindo ao banco DIO Sr. {nome}!
Qual operação deseja realizar hoje?""")
print('-=-' * 17)

while True:

    op = int(input(menu))

    if op == 1 :
        print('\033[1:32mDEPOSITO.....\033[m')
        valor = float(input('Qual o valor:R$  '))
        print('-=-' * 17)
        if valor > 0:
            saldo += valor
            extra += f'Depósito : .... R${valor:.2f}\n'
            print(f'\033[1:32mDespósito de R$ {valor:.2f} realizado com Sucesso!\033[m')
            print('-=-' * 17)

        else:
            print('\033[1:31mOperação falhou! O valor informado é inválido.\033[m')
            print('-=-' * 17)

    elif op == 2:
        print('\033[1:33mSACAR......\033[m')
        valor = float(input('Qual valor:R$ '))
        print('-=-' * 17)

        if valor > saldo:
            print('\033[1:31mOperação Falhou! Saldo Insuficiente.\033[m')
            tentSaques += 1
            print('-=-' * 17)

        elif valor >= limite:
            print(f'\033[1:31mOperação falhou!O valor {valor} excedeu o limide de R$500.\033[m')
            tentSaques += 1
            print('-=-' * 17)

        elif numSaques > limSaques:
            print(f'\033[1:31mOperação Falhou! Excedeu o limite de saques de {limSaques} diarios.\033[m')
            tentSaques += 1
            print('-=-' * 20)

        elif valor > 0:
            saldo -= valor
            extra += f'Saque {numSaques}  : .... R${valor:.2f}\n'
            numSaques += 1
            print(f'\033[1:32mSaque realizado com SUCESSO! Valor R${valor}\033[m')
            print('-=-' * 17)

        else:
            print('\033[1:31mOperaçãos Falhou! O valor informado é inválido.\033[m')
            tentSaques += 1
            print('-=-' * 17)

    elif op == 3:
        print(f'\n{"\033[4mEXTRATO\033[m":^27}')
        if extra == '':
            print(f'\033[1:34mNenhuma movimentação até o momento.\033[m')
        else:
            print(extra,end='')
            print(f'Info     : .... {tentSaques} tentativas de saques não permitidos.')
            print(f'Saldo    : .... R${saldo:.2f}')
            print('-=-'*17)
    elif op == 4:
        print(f'VOLTE SEMPE SR. {nome}!')
        print('FINALIZANDO............')
        print('-=-' * 17)
        break

    else:
        print('\033[1:34mOperação inválida, por favor selecione uma opção valida!\033[m')
        print('-=-' * 17)
