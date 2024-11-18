# 2. (Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar.

print('Verificador de número PAR ou ÍMPAR!')

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O numéro digitado "{num}" é PAR!')
else:
    print(f'O numéro digitado "{num}" é ÍMPAR!')