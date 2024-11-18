# (Jogo de Adivinhação)
# Implemente um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o
# usuário deve adivinhar. Após cada tentativa, diga se o número é maior ou menor que o
# número secreto, e conte o número de tentativas até acertar.
print('Jogo de Adivinhação!!')

import random
print('Adivinhe qual número estou pensando, ele está entre 1 e 100!!')

num = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input('Digite um número: '))
    tentativas += 1

    if chute < num:
        print('O número secreto é maior!')
    elif chute > num:
        print('O número secreto é menor!')
    else:
        print(f'Parabéns! Você acertou o número que eu estava pensando "{num}" em {tentativas} tentativas')
    break
