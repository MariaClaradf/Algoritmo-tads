# 3. (Calculadora Básica com Estruturas Condicionais) Peça ao usuário dois números e
# uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.

print('calculadora básica com estruturas condicionais!!')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = input('Escolha uma operação (+, -, *, /): ')

def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return "Operação inválida!"

result = calcular(n1, n2, op)
print('Resultado:', result)
