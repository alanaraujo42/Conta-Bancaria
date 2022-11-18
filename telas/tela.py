from desenvolvimento.login_contacorrente import login
from time import sleep


class Tela:

    def tela_inicial(self):
        print('-' * 5, 'Seja bem vindo ao Banco', '-' * 5)
        print('''
OPÇÕES:
1- Login na sua conta
2- Cadastrar conta
0- Sair do Banco
        ''')
        while True:
            resposta = input('Digite o número correspondente a sua escolha: ')
            resposta = resposta.strip()
            if resposta == '1' or resposta == '2' or resposta == '0':
                return resposta
            else:
                print('\nERRO: Digite somente os números disponiveis')

    def tela_login(self):
        print('\n' * 30)
        print(' ----- LOGIN ----\nDigite as infromações para login\n')
        resposta = login()
        return resposta

    def tela_opcoes_da_conta(self, conta):
        print('\n' * 30)
        print(f'''
        Bem vindo(a): {conta.nome}
        Agência: {conta.agencia}
        Conta: {conta.numero_conta}
        Saldo: R${conta.saldo}

------------- OPÇÕES -------------
        1- Sacar Dinheiro
        2- Depositar dinheiro
        0- Sair da conta
        ''')
        while True:
            resposta = input('Digite o número da sua opção: ')
            resposta = resposta.strip()
            if resposta == '1' or resposta == '2' or resposta == '0':
                return resposta
            else:
                print('\nDigite somenete as opções disponíveis')

    def tela_cadastro_nao_existe(self):
        print('''
ERRO: Cadastro não existe!
Gostaria de realizar cadastro?
1- Sim
2- Não
            ''')
        while True:
            resposta = input('Digite a sua opção: ')
            if resposta == '1' or resposta == '2':
                return resposta
            else:
                print('ERRO: Digite as opções disponíveis')

    def tela_apos_cadastro(self):
        print(' ---- Cadastro Realizado com Sucesso ----')
        sleep(2)
        print('Você já pode realizar o Login na sua conta')
        print('\nVoltando a tela inicial')
        sleep(3)
        print('\n' * 30)

    def tela_cadastro_ja_existente(self):
        print('CPF já Cadastrado')
        print('Voltando para Tela Inicial')
        sleep(3)
        print('\n' * 30)

    def tela_saque_dinheiro(self, conta):
        print('\n' * 30)
        print('---- Saque de Dinheiro ----')
        while True:
            valor = input('Digite o valor que você deseja sacar: R$')
            valor = valor.strip()
            valor_reserva = valor
            valor = valor.replace(',', '')
            if valor.isnumeric():
                valor = valor_reserva
                valor = valor.replace(',', '.')
                valor = float(valor)
                resposta = conta.sacar_dinheiro(valor)
                if resposta:
                    print(f'Saque de R${valor} realizado com sucesso')
                    sleep(3)
                    break
                else:
                    print('Saque NÃO realizado\nSaldo Insuficente')
                    sleep(3)
                    break
            else:
                print('\nERRO: Digite somente números')

    def tela_deposito_dinheiro(self, conta):
        print('\n' * 30)
        print('---- Deposito de Dinheiro ----')
        while True:
            valor = input('Digite o valor que você deseja depositar: R$')
            valor = valor.strip()
            valor_reserva = valor
            valor = valor.replace(',', '')
            if valor.isnumeric():
                valor = valor_reserva
                valor = valor.replace(',', '.')
                valor = float(valor)
                conta.depositar_dinheiro(valor)
                print(f'Deposito de R${valor} realizado com sucesso')
                sleep(3)
                break
            else:
                print('\nERRO: Digite somente números')
