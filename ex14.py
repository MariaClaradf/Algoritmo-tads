# (Verificador de Palíndromos) Receba uma palavra e determine se ela é um palíndromo
# (ou seja, se lê igual de trás para frente).

print('Verificador de Palíndromos!!')

plvr = input('Digite uma palavra: ')
inverso = plvr[::-1]

if plvr == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')    