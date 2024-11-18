# (Contador de Caracteres de uma Frase) Receba uma frase e retorne um dicionário
# que contém a quantidade de cada caractere (inclusive espaços).

print('Contador de caracteres de uma frase!!')

frase = input('Digite uma frase: ')
qntd = {}

for caractere in frase:
    if caractere in qntd:
        qntd[caractere] += 1
    else:
        qntd[caractere] = 1

print('Quantidade de caractere na frase: ')
print(qntd)
