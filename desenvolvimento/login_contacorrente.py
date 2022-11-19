from desenvolvimento.banco_de_dados import banco_de_contas


def login_cpf():
    while True:
        cpf = input('Digite o seu CPF (somente números): ')
        # Tratamento do dado
        cpf = cpf.strip()
        cpf = cpf.replace(' ', '')
        # Verificação do dado
        if cpf.isnumeric() and len(cpf) == 11:
            return cpf
        else:
            print('ERRO: CPF Inválido!')


def login_senha():
    while True:
        senha = input('Digite sua senha com 4 dígitos: ')
        senha = senha.strip()
        if len(senha) == 4 and senha.isnumeric():
            return senha
        else:
            print('ERRO: Somente 4 dígitos e números')


def verificação_banco_de_dados(cpf, senha):
    for conta in banco_de_contas:
        dado_cpf = conta.cpf
        dado_senha = conta.senha
        if cpf == dado_cpf and senha == dado_senha:
            return conta
    return 'Você não possui cadastro!'


def login():
    # Input dos dados de login
    cpf = login_cpf()
    senha = login_senha()
    # Verificação dos dados no banco de dados
    resultado = verificação_banco_de_dados(cpf, senha)
    return resultado
