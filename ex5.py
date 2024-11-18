# (Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10).

print('Gerador de Tabuada!')

num = int(input('Digite um número e veja a tabuada correspondente: '))
print(f'Tabuada do {num}')

for i in range(1, 11):
    result = num * i
    print(f'{num} x {i} = {result}')
 