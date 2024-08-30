# Calculadora.py

class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao='+'):
        self._valorA = valorA
        self._valorB = valorB
        self._operacao = operacao

    @property
    def valorA(self):
        return self._valorA

    @valorA.setter
    def valorA(self, valor):
        self._valorA = valor

    @property
    def valorB(self):
        return self._valorB

    @valorB.setter
    def valorB(self, valor):
        self._valorB = valor

    @property
    def operacao(self):
        return self._operacao

    @operacao.setter
    def operacao(self, operacao):
        self._operacao = operacao

    def validarOperacao(self, operacao):
        operacoes_validas = ['+', '-', '*', '/']
        return operacao in operacoes_validas

    def calcular(self):
        if not self.validarOperacao(self._operacao):
            print("Operação inválida!")
            exit(1)

        if self._operacao == '+':
            return self._valorA + self._valorB
        elif self._operacao == '-':
            return self._valorA - self._valorB
        elif self._operacao == '*':
            return self._valorA * self._valorB
        elif self._operacao == '/':
            if self._valorB == 0:
                print("Erro: Divisão por zero!")
                exit(1)
            return self._valorA / self._valorB

    def mostrarResultado(self):
        print(f"{self._valorA} {self._operacao} {self._valorB} = {self.calcular()}")

    def entradaDados(self):
        self._valorA = float(input("Digite o primeiro valor: "))
        self._operacao = input("Digite a operação (+, -, *, /): ")
        self._valorB = float(input("Digite o segundo valor: "))
       
