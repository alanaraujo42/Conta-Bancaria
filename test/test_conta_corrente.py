import pytest
from desenvolvimento.conta_corrente import ContaCorrente


@pytest.fixture
def conta():
    return ContaCorrente('Alan Araújo Santos', '11122233344', '1234')


def test_cadastro_nome(conta):
    assert isinstance(conta.nome, str)


def test_cadastro_cpf(conta):
    assert conta.cpf.isnumeric() and len(conta.cpf) == 11


def test_cadastrar_senha(conta):
    assert isinstance(conta.senha, str) and len(conta.senha) == 4


def test_cadastro_agencia(conta):
    assert isinstance(conta.agencia, str) and len(conta.agencia) == 4


def test_cadastro_numero_conta(conta):
    assert isinstance(conta.numero_conta, str) and len(conta.numero_conta) == 5


def test_conta(conta):
    assert isinstance(conta, ContaCorrente)
