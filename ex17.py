# (Ordenação de Lista com Números Negativos e Positivos) Dada uma lista de números inteiros que incluem positivos e negativos, ordene-os de forma que os negativos fiquem
# antes dos positivos, mantendo a ordem original relativa entre eles.

print('Ordenação de Lista com Números Negativos e Positivos!!')


num = input('Digite os números desejados separando-os com espaço: ')
num = [int(n) for n in num.split()]


negativo = []
positivo = []

for number in num:
    if number < 0:
        negativo.append(number)
    else:
        positivo.append(number)


result = negativo + positivo

print(f'Lista inicial: {num}')
print(f'Lista ordenada: {result}')
