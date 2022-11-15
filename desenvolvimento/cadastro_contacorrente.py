from conta_corrente import ContaCorrente
from banco_de_dados import banco_de_contas


def cadastro_nome():
    while True:
        nome = input('Digite o seu nome completo: ')
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
        if x == True:
            return nome
        else:
            print('ERRO: Digite somente palavras!')


def cadastro_cpf():
    while True:
        cpf = input('Digite o seu CPF (somente números): ')
        # Tratamento do dado
        cpf = cpf.strip()
        # Verificação do dado
        if cpf.isnumeric() and len(cpf) == 11:
            return cpf
        else:
            print('ERRO: CPF Inválido!')


def cadastro_senha():
    while True:
        senha = input('Digite uma senha com 4 dígitos: ')
        senha = senha.strip()
        if len(senha) == 4 and senha.isnumeric():
            return senha
        else:
            print('ERRO: Somente 4 dígitos e números')


def cadastro_conta_corrente():
    # Input de dados
    nome = cadastro_nome()
    cpf = cadastro_cpf()
    senha = cadastro_senha()
    # Criação de conta corrente com os dados
    conta = ContaCorrente(nome, cpf, senha)
    # Salavamento da conta no Banco de Dados
    banco_de_contas.append(conta)
    return conta
