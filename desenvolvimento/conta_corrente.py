class ContaCorrente:

    def __init__(self, nome=str, cpf=int, senha=str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.agencia = '0001'
        self.numero_conta = '12345'
        self.saldo = 0
        self.historico_transacoes = []

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        self.historico_transacoes.append(f'DEPOSITO: R${valor}')

    def verificar_saldo(self, valor):
        if valor <= self.saldo:
            return True
        else:
            return False

    def sacar_dinheiro(self, valor):
        """"
        Função que vai verificar o saldo da conta e realizar saque,
        se valor menor ou igual ao saldo da e retornar True, caso
        contrátrio, False.
        """
        if ContaCorrente.verificar_saldo(self, valor):
            self.saldo -= valor
            self.historico_transacoes.append(f'SAQUE: R${valor}')
            return True
        else:
            return False

    def transferir_dinheiro(self, conta_destino, valor):
        self.saldo -= valor
        conta_destino.saldo += valor
        self.historico_transacoes.append(
            f'TRANSFERÊNCIA - PARA: {conta_destino.nome} - VALOR: R${valor}')
        conta_destino.historico_transacoes.append(
            f'TRANSFERÊNCIA - DE: {self.nome} - VALOR: R${valor}')
