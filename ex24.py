# (Verificação de Anagrama) Receba duas palavras e determine se elas são anagramas
# (ou seja, possuem as mesmas letras em qualquer ordem).

print('Verificação de anagrama!!')

plvr1 = input('Digite a primeira palavra: ')
plvr2 = input('Digite a segunda palavra: ')

def verificacao(plvr1, plvr2):
    if len(plvr1) != len(plvr2):
        return False
    
    for letra in plvr1:
        if plvr1.count(letra) != plvr2.count(letra):
            return False
    
    return True

if verificacao(plvr1, plvr2):
    print('Elas são anagramas!')
else: 
    print('Elas não são anagramas!')

