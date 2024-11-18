# (Verificador de Maioridade) Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.

print('Verificador de maioridade')

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Você é de maioridade!')
else:
    print('Você é de menoridade!')