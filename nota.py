# Função para converter nota numérica em conceito
def converter_nota(nota):
    if nota == 0:
        return 'E'
    elif 1 <= nota <= 35:
        return 'D'
    elif 36 <= nota <= 60:
        return 'C'
    elif 61 <= nota <= 85:
        return 'B'
    elif 86 <= nota <= 100:
        return 'A'
    else:
        return 'Nota inválida'

# Leitura da entrada
nota = int(input())

# Impressão do conceito correspondente
print(converter_nota(nota))
