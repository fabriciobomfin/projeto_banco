import pytest
from banco.models.conta import Conta

@pytest.fixture 
def conta_valida():
    conta = Conta(333, 444)
    
def test_validando_atributo_numero_conta(conta_valida):
    assert conta_valida.numero_conta == 333

def test_validando_atributo_numero_agencia(conta_valida):
    assert conta_valida.agencia == 444

def test_validando_atributo_numero_saldo(conta_valida):
    assert conta_valida._saldo == 0

def test_depositar_valor_positivo(conta_valida):
    conta_validade.depositar(100)
    assert conta_valida._saldo == (100)
