# . (Remoção de Elementos Duplicados) Receba uma lista de inteiros e retorne uma nova
# lista sem elementos duplicados, mantendo a ordem original

print('Remoção de Elementos Duplicados')

lista = [1, 2, 3, 1, 7, 8, 3, 10, 2]

def remove(list):
    new = []
    for elemento in list:
        if elemento not in new:
            new.append(elemento)
    return new

result = remove(lista)
print(result)

