conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre conjunto 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre conjunto 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_Diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("A diferença simétrica é: {}" .format(conjunto_Diff_simetrica))

conjuntoA = {1,2,3}
conjuntoB = {1,2,3,4,5}
conjunto_subset = conjuntoA.issubset(conjuntoB)
print('Conjunto A é um subconjunto de B?: {}'.format(conjunto_subset))
conjunto_superset = conjuntoA.issuperset(conjuntoB)
print('Conjunto A é um superconjunto de B?: {}'.format(conjunto_superset))

# CONVERSÕES DE LISTA PARA CONJUNTO. A IDEIA É REMOVER DUPLICIDADES.

lista = ['cachorro', 'gato', 'elefante', 'cachorro', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

#CONVERTENDO DE VOLTA PARA LISTA. AGORA SEM ITENS DUPLICADOS:

lista_animais = list(conjunto_animais)
print(lista_animais)

# #Conjuntos não permitem duplicidades:
# conjunto = {1,2,3,4,4,2}
# print(conjunto)
# #Adicionar e retirar item no cojunto:
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)