import textwrap

def menu():
    menu = """
    ==========MENU DE OPERAÇÕES========
              [1]DEPOSITAR
              [2]SACAR
              [3]EXTRATO
              [4]NOVA CONTA
              [5]LISTAR CONTAS
              [6]NOVO USUÁRIO
              [7]SAIR
   ==> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo +=valor
        extrato += f'Depósito : .... R${valor:.2f}\n'
        print(f'\033[1:32mDespósito de R$ {valor:.2f} realizado com Sucesso!\033[m')

    else:
        print('\033[1:31mOperação falhou! O valor informado é inválido.\033[m')
        print('-=-' * 17)

    return saldo,extrato


def sacar(*,saldo, valor, extrato, limite, num_saques, lim_saques):

        if valor > saldo:
            print('\033[1:31mOperação Falhou! Saldo Insuficiente.\033[m')

            print('-=-' * 17)

        elif valor >= limite:
            print(f'\033[1:31mOperação falhou!O valor {valor} excedeu o limide de R$500.\033[m')

            print('-=-' * 17)

        elif num_saques >= lim_saques:
            print(f'\033[1:31mOperação Falhou! Excedeu o limite de saques de {lim_saques} diarios.\033[m')

            print('-=-' * 20)

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque {num_saques}  : .... R${valor:.2f}\n'
            num_saques += 1
            print(f'\033[1:32mSaque realizado com SUCESSO! Valor R${valor}\033[m')
            print('-=-' * 17)

        else:
            print('\033[1:31mOperaçãos Falhou! O valor informado é inválido.\033[m')

            print('-=-' * 17)
        return saldo, extrato , num_saques, lim_saques


def exibir_extrato(saldo,/,*,extrato):

        print(f'\n{"\033[4mEXTRATO\033[m":^27}')
        if extrato == '':
            print(f'\033[1:34mNenhuma movimentação até o momento.\033[m')
        else:
            print(extrato,end='')
            print(f'Saldo    : .... R${saldo:.2f}')
            print('-=-'*17)


def criar_usuario(usuarios):
    cpf = input('Informe seu CPF(somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\033[1:31mJa existe usuário com esse CPF\033[m')
        return

    nome = input('Informe seu nome: ')
    data_nascimento = input('informe a data de nascimento dd-mm-aaaa: ')
    endereco = input('Endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome':nome, 'data de nascimento':data_nascimento, 'cpf':cpf, 'endereço':endereco})

    print('\033[1:32m Usuário criado com sucesso!\033[m')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\033[1:32m\n=== Conta criada com sucesso! ===\033[m")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(f'\033[1:31m{"\n Usuário não encontrado, fluxo de criação de conta encerrado!"}\033[m')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    lim_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 1
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            print('\033[1:33mSACAR......\033[m')
            valor = float(input('Qual valor:R$ '))
            print('-=-' * 17)

            saldo, extrato, num_saques, lim_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                lim_saques=lim_saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            break

        else:
            print("\033[1:31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")


main()