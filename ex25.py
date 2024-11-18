# (Filtro de Números Pares em uma Lista) Receba uma lista de inteiros e filtre apenas os números pares.

print('Filtro de números pares em uma lista!!')

lista = input('Digite alguns números para formar a lista, separando eles com espaço: ').split()
lista = [int(n) for n in lista]
pares = [n for n in lista if n % 2 == 0]

print('Números pares:', pares)


