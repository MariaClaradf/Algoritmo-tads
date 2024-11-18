# (Números Primos em um Intervalo) Receba um intervalo de números do usuário (por exemplo, entre 10 e 50)
# e retorne uma lista com todos os números primos dentro desse intervalo.

print('Números Primos em um Intervalo!!')

primeiro = int(input('Digite o início do intervalo: '))
ultimo = int(input('Digite o fim do itervalo: '))
primos = []

for num in range(primeiro, ultimo + 1):
    if num < 2:
        continue
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
        if primo:
            primos.append(num)

print(f'Os números primos do intervalo {primeiro} e {ultimo} são: {primos}')
