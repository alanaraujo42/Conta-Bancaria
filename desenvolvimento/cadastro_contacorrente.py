from desenvolvimento.conta_corrente import ContaCorrente
from desenvolvimento.banco_de_dados import banco_de_contas


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
        if x:
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


def verificar_banco_de_dados(cpf):
    for conta in banco_de_contas:
        verificar_cpf = conta.cpf
        if cpf == verificar_cpf:
            return 'ERRO'
    return None


def cadastro_conta_corrente():
    print('\n' * 30)
    print('----- Cadastro de Conta Corrente -----')
    # Input de dados
    nome = cadastro_nome()
    cpf = cadastro_cpf()
    # Verificar se CPF já existe no Banco De Dados
    resposta = verificar_banco_de_dados(cpf)
    if resposta == 'ERRO':
        return resposta
    senha = cadastro_senha()
    # Criação de conta corrente com os dados
    conta = ContaCorrente(nome, cpf, senha)
    # Salavamento da conta no Banco de Dados
    banco_de_contas.append(conta)
    return conta
