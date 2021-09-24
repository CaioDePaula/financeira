import pytest
from faker import Faker
from app.financeira import Financeira


def test_tipo_saldo():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    saldo = financeira.visualizar_saldo()
    assert isinstance(saldo, float)


def test_valor_saldo_correto():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    saldo = financeira.visualizar_saldo()
    assert deposito == saldo


def test_deposito():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    financeira.deposito(deposito)
    saldo = financeira.visualizar_saldo()
    assert saldo == 2000.0


def test_deposito_valor_invalido():
    with pytest.raises(ValueError, match='valor de deposito invalido'):
        fake_data_generate = Faker()
        nome = fake_data_generate.name()
        deposito = 1000.00
        financeira = Financeira(nome, deposito)
        financeira.deposito(nome)


def test_deposito_valor_abaixo_minimo():
    with pytest.raises(ValueError, match=r'valor de deposito menor que o permitido que é de'):
        fake_data_generate = Faker()
        nome = fake_data_generate.name()
        deposito = 1000.00
        financeira = Financeira(nome, deposito)
        novo_deposito = 0.5
        financeira.deposito(novo_deposito)


def test_deposito_retorno_vazio():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    novo_deposito = 1.5
    resultado = financeira.deposito(novo_deposito)
    assert not resultado


def test_sacar():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    financeira.deposito(deposito)
    valor_saque = 1500.00
    financeira.sacar(valor_saque)
    saldo = financeira.visualizar_saldo()
    assert saldo == 500.00


def test_sacar_valor_invalido():
    with pytest.raises(ValueError, match='valor de saque invalido'):
        fake_data_generate = Faker()
        nome = fake_data_generate.name()
        deposito = 1000.00
        financeira = Financeira(nome, deposito)
        financeira.sacar(nome)


def test_sacar_valor_acima_limite():
    with pytest.raises(ValueError, match='você não possui saldo suficiente'):
        fake_data_generate = Faker()
        nome = fake_data_generate.name()
        deposito = 1000.00
        financeira = Financeira(nome, deposito)
        valor_saque = 1500.00
        financeira.sacar(valor_saque)


def test_sacar_retorno_vazio():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    valor_saque = 1.5
    resultado = financeira.sacar(valor_saque)
    assert not resultado


def test_tipo_taxa_juros():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    taxa = financeira.visualizar_taxa_juros()
    assert isinstance(taxa, float)


def test_valor_taxa_juros():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    taxa = financeira.visualizar_taxa_juros()
    assert taxa == 0.05


def test_tipo_emprestimo():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    valor_emprestimo = 2000.00
    valor_divida = financeira.emprestimo(valor_emprestimo)
    assert isinstance(valor_divida, float)


def test_emprestimo():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    valor_emprestimo = 2000.00
    valor_divida = financeira.emprestimo(valor_emprestimo)
    valor_esperado = valor_emprestimo + (valor_emprestimo * financeira.visualizar_taxa_juros())
    assert valor_divida == valor_esperado


def test_emprestimo_valor_invalido():
    with pytest.raises(ValueError, match='valor de emprestimo invalido'):
        fake_data_generate = Faker()
        nome = fake_data_generate.name()
        deposito = 1000.00
        financeira = Financeira(nome, deposito)
        valor_emprestimo = 2000
        financeira.emprestimo(valor_emprestimo)


def test_emprestimo_valor_abaixo_limite():
    with pytest.raises(ValueError, match='valor de emprestimo menor do que o permitido! o valor minimo é'):
        fake_data_generate = Faker()
        nome = fake_data_generate.name()
        deposito = 1000.00
        financeira = Financeira(nome, deposito)
        valor_emprestimo = 10.00
        financeira.emprestimo(valor_emprestimo)


def test_extrato():
    fake_data_generate = Faker()
    nome = fake_data_generate.name()
    divida = 0.00
    deposito = 1000.00
    financeira = Financeira(nome, deposito)
    extrato = financeira.extrato()
    extrato_esperado = {
        'saldo': deposito,
        'divida': divida
    }
    assert extrato == extrato_esperado
