a = int(input("Primeiro bimestre: "))
if a > 10:
    a = int(input('Você digitou uma nota maior que o permitido. Primeiro bimestre: '))

b = int(input("Segundo bimestre: "))
if b > 10:
    b = int(input('Você digitou uma nota maior que o permitido. Segundo bimestre: '))

c = int(input("Terceiro bimestre: "))
if c > 10:
    c = int(input('Você digitou uma nota maior que o permitido. Terceiro bimestre: '))

d = int(input("Quarto bimestre: "))
if d > 10:
    d = int(input('Você digitou uma nota maior que o permitido. Quarto bimestre: '))

media = (a+b+c+d)/4

print('Média: {} '. format(media))
# if a<=10 and b<=10 and c<=10 and d<=10:
#     print('media: {}'. format(media))
# else:
#     print('Foi digitado alguma nota errada!')

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0 :
#     print('Há um número par entre os digitados.')
# else:
#     print('Nenhum número par foi digitado.')


# a = int (input('Primeiro valor: '))
# b = int (input('Segundo valor: '))
# c = int(input('Terceiro número '))
#
# if a > b and a > c:
#     print("O maior número é {}.".format(a))
# elif b > a and b > c:
#     print('O Maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print("Final do programa")