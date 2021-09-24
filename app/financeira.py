class Financeira:
    def __init__(self, nome: str, deposito: float) -> None:
        self.nome: str = nome
        self.divida: float = 0
        self.saldo: float = deposito
        self.taxa_juros: float = 0.05
        self.valor_minimo_deposito: float = 1.00
        self.valor_minimo_emprestimo: float = 500.00

    def deposito(self, valor: float) -> None:
        if not isinstance(valor, float):
            raise ValueError('valor de deposito invalido')

        if valor < self.valor_minimo_deposito:
            raise ValueError('valor de deposito menor que o permitido que é de {}'.format(
                self.valor_minimo_deposito))

        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if not isinstance(valor, float):
            raise ValueError('valor de saque invalido')

        if valor > self.saldo:
            raise ValueError('você não possui saldo suficiente')

        self.saldo -= valor

    def visualizar_taxa_juros(self) -> float:
        return self.taxa_juros

    def emprestimo(self, valor: float) -> float:
        if not isinstance(valor, float):
            raise ValueError('valor de emprestimo invalido')

        if valor < self.valor_minimo_emprestimo:
            raise ValueError('valor de emprestimo menor do que o permitido! o valor minimo é: {}'.format(
                self.valor_minimo_emprestimo))

        juros = valor * self.taxa_juros
        valor_divida = valor + juros
        self.divida += valor_divida
        return self.divida

    def visualizar_saldo(self) -> float:
        return self.saldo

    def visualizar_divida(self) -> float:
        return self.divida

    def extrato(self) -> float:
        extrato_dados = {
            'saldo': self.saldo,
            'divida': self.divida
        }

        return extrato_dados
