# (Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de
# vogais e consoantes. Ignore espaços e caracteres especiais.

print('Contagem de vogais e consoantes!!')

def contagem(plvr):
    vogais = 'aeiou'
    cont_vogais = cont_consoantes = 0

    for char in plvr:
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in vogais:
                cont_vogais += 1
            else:    
                cont_consoantes += 1
    return cont_vogais, cont_consoantes            

plvr = input('Digite uma frase: ').lower()
vogais, consoantes = contagem(plvr)

print(f'Vogais: {vogais}')
print(f'Consoantes: {consoantes}')
 
