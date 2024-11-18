# . (Gerador de Números da Sequência de Fibonacci) Peça ao usuário um número n e
# gere uma lista com os n primeiros números da sequência de Fibonacci.

print('Gerador de Númeroa da sequência de Fibonacci')

num = int(input('Digite um número para gerar os n primeiros números da sequência Fibonacci: '))
f = [0, 1]

for i in range(2, num):
    nnum = f[-1] + f[-2]
    f.append(nnum)

print(f'Os primeiros {num} números da sequência fibonacci são: {f[:num]}')

