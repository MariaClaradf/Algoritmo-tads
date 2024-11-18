# (Média com Notas Maiores que a Média) Peça uma lista de notas de alunos e calcule
# a média. Em seguida, retorne uma lista com as notas que são maiores do que a média.

notas = [float(input(f'Digite a nota {i + 1}: ')) for i in range(int(input('Quantas notas deseja inserir para calcular a média? ')))]
media = sum(notas) / len(notas)

print(f'A média das notas é: {media:.2f}')
print('Notas maiores que a média:', [nota for nota in notas if nota > media])
