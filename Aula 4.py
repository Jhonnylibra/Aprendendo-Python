a = int(input("Primeiro bimestre: "))
while a > 10:
    a = int(input('Você digitou uma nota maior que o permitido. Primeiro bimestre: '))

b = int(input("Segundo bimestre: "))
while b > 10:
    b = int(input('Você digitou uma nota maior que o permitido. Segundo bimestre: '))

c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input('Você digitou uma nota maior que o permitido. Terceiro bimestre: '))

d = int(input("Quarto bimestre: "))
while d > 10:
    d = int(input('Você digitou uma nota maior que o permitido. Quarto bimestre: '))

media = (a+b+c+d)/4

print('Média: {} '. format(media))

# IMPRIMI TODOS OS NUMEROS PRIMOS EM UMA SEQUENCIA DETERMINADA DENTRO DO LAÇO "FOR"
# for i in range(1001):
#     div = 0
#
#     for x in range(1, i+1):
#         resto = i % x
#         #print(x,resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#
#         print(i)

# INFORMA SE UM NUMERO DIGITADO É PRIMO OU NÃO COM O COMANDO "FOR"
# a= int(input('Entre com um número: '))
#
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     print(x,resto)
#     if resto == 0:
#         div += 1
#
# if div ==2:
#
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

#CALCULA A MEDIA DE 4 BIMESTRES USANDO DO COMANDO "IF"
# a = int(input("Primeiro bimestre: "))
# if a > 10:
#     a = int(input('Você digitou uma nota maior que o permitido. Primeiro bimestre: '))
#
# b = int(input("Segundo bimestre: "))
# if b > 10:
#     b = int(input('Você digitou uma nota maior que o permitido. Segundo bimestre: '))
#
# c = int(input("Terceiro bimestre: "))
# if c > 10:
#     c = int(input('Você digitou uma nota maior que o permitido. Terceiro bimestre: '))
#
# d = int(input("Quarto bimestre: "))
# if d > 10:
#     d = int(input('Você digitou uma nota maior que o permitido. Quarto bimestre: '))
#
# media = (a+b+c+d)/4
#
# print('Média: {} '. format(media))