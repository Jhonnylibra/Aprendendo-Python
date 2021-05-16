a = float(input('Entre com o primeiro valor: '))
b = float(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print("Soma: {soma}. \nSubtração: {subtracao}. \nMultiplicação: {multi}."
      "\nDivisão: {div}.""\nresto: {resto}.".format(soma=soma, subtracao=subtracao,
                                                    multi=multiplicacao, div=divisao, resto=resto))
