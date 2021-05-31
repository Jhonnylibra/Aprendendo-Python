
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    # Funções retornam valores
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multip(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculo = Calculadora (10,2)

print(calculo.valor_a)
print(calculo.soma())
print(calculo.subtracao())
print(calculo.multip())
print(calculo.divisao())
