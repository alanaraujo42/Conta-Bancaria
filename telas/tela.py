from desenvolvimento.login_contacorrente import login
from desenvolvimento.banco_de_dados import banco_de_contas
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
        3- Tranferir dinheiro
        4- Histórico de transações
        0- Sair da conta
        ''')
        while True:
            resposta = input('Digite o número da sua opção: ')
            resposta = resposta.strip()
            if resposta == '1' or resposta == '2' or \
                    resposta == '0' or resposta == '3' or resposta == '4':
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

    def _verifcar_valor(valor):
        valor = valor.strip()
        valor_reserva = valor
        valor = valor.replace(',', '')
        if valor.isnumeric():
            valor = valor_reserva
            valor = valor.replace(',', '.')
            valor = float(valor)
            return valor
        else:
            print('\nERRO: Digite somente números')

    def tela_saque_dinheiro(self, conta):
        print('\n' * 30)
        print('---- Saque de Dinheiro ----')
        while True:
            while True:
                valor = input('Digite o valor que você deseja sacar: R$')
                resultado = Tela._verifcar_valor(valor)
                if isinstance(resultado, float):
                    valor = resultado
                    break
            resposta = conta.sacar_dinheiro(valor)
            if resposta:
                print(f'Saque de R${valor} realizado com sucesso')
                sleep(3)
                break
            else:
                print('Saque NÃO realizado\nSaldo Insuficente')
                sleep(3)
                break

    def tela_deposito_dinheiro(self, conta):
        print('\n' * 30)
        print('---- Deposito de Dinheiro ----')
        while True:
            while True:
                valor = input('Digite o valor que você deseja depositar: R$')
                resultado = Tela._verifcar_valor(valor)
                if isinstance(resultado, float):
                    valor = resultado
                    break
            conta.depositar_dinheiro(valor)
            print(f'Deposito de R${valor} realizado com sucesso')
            sleep(3)
            break

    def _pegar_nome():
        while True:
            nome = input('Digite o nome completo da pessoa: ')
            # Tratamento do nome
            nome = nome.strip()
            nome = nome.title()
            # Verificação de nome
            verificação = nome.split()
            for i in verificação:
                if i.isalpha():
                    x = True
                else:
                    x = False
                    break
            if x:
                return nome
            else:
                print('ERRO: Digite somente palavras!')

    def _pegar_cpf():
        while True:
            cpf = input('Digite o CPF da pessoa (somente números): ')
            # Tratamento do dado
            cpf = cpf.strip()
            # Verificação do dado
            if cpf.isnumeric() and len(cpf) == 11:
                return cpf
            else:
                print('ERRO: CPF Inválido!')

    # Verificação para transferência
    def _verificação_banco_de_dados(cpf, nome):
        for conta in banco_de_contas:
            dado_cpf = conta.cpf
            dado_nome = conta.nome
            if cpf == dado_cpf and nome == dado_nome:
                return conta
        return 'Você não possui cadastro!'

    def tela_transferir_dinheiro(self, conta):
        print('\n' * 30)
        print('---- Transferencia de dinheiro ----')
        print('-- Dados da conta Destino:')
        while True:  # Verificação no Banco De Dados
            nome = Tela._pegar_nome()
            cpf = Tela._pegar_cpf()
            resultado = Tela._verificação_banco_de_dados(cpf, nome)
            if isinstance(resultado, str):
                print('ERRO: Conta não existe!')
                sleep(3)
                break
            conta_destino = resultado
            while True:  # Verificar valor digitado
                valor = input('Digite o valor que você deseja transferir: R$')
                resultado = Tela._verifcar_valor(valor)
                if isinstance(resultado, float):
                    valor = resultado
                    break
            x = conta.verificar_saldo(valor)  # Verificar saldo
            if x:  # Realização da transferência
                conta.transferir_dinheiro(conta_destino, valor)
                print(f'''
---- Transferência realizada com sucesso ----
        Valor transferido: R${valor}
        Pessoa: {conta_destino.nome}
        CPF: {conta_destino.cpf}
                ''')
                sleep(4)
                break
            else:  # Saldo insuficênte na conta
                print('---- Saldo insuficiênte ----')
                sleep(3)
                break

    def tela_historico_transacoes(self, conta):
        print('\n' * 30)
        print('---- SEU HISTÓRICO DE TRANSAÇÕES ----')
        for transferencia in conta.historico_transacoes:
            print(transferencia)
            sleep(0.5)
        input('\nClique em qualquer tecla para voltar')
