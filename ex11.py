# (Contador de Palavras Únicas) Peça ao usuário uma frase e, em seguida, conte quantas
# palavras únicas ela possui (sem considerar maiúsculas e minúsculas).

print('Contador de Palavras Únicas!!')

frase = input('Digite uma frase: ')
plvr = frase.lower().split()
unicas = []

for palavra in plvr:
    if palavra not in unicas:
        unicas.append(palavra)

qntd = len(unicas)
print(f'A frase possui {qntd} palavras únicas!') 

