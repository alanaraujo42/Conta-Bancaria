class ContaCorrente:

    def __init__(self, nome=str, cpf=int, senha=str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.agencia = '0001'
        self.numero_conta = '12345'
        self.saldo = 0

    def depositar_dinheiro(self, valor):
        self.saldo += valor

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
        if ContaCorrente.verificar_saldo(valor):
            self.saldo -= valor
            return True
        else:
            return False
