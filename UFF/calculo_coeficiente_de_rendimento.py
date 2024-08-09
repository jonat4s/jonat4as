""" Aqui como calcular o CR ( coeficiente de rendimento ) para alunos da UFF, utilizando dados aleatórios como exemplo """

# Insira as notas das disciplinas ( abaixo como converter string em float para facilitar)

# Indique a quantidade de disciplinas
tamanho = int(input("Digite o número de disciplinas: "))

# Inicializa as listas para armazenar notas e cargas horárias
notas = []
cargas_horarias = []

# Coleta as notas e as cargas horárias (sempre inserir a nota com .)
for i in range(tamanho):
    nota = float(input(f"Digite a nota da disciplina {i + 1}: "))
    carga_horaria = float(input(f"Digite a carga horária da disciplina {i + 1}: "))
    
    # Adiciona os valores às listas
    notas.append(nota)
    cargas_horarias.append(carga_horaria)

# Função que calcula o CR a partir dos dados dispostos

def cr(notas, carga_horaria):

    return sum(x * y for x, y in zip(notas, carga_horaria)) / sum(carga_horaria)


# Chamando a função e calculando o CR arredondando a média.
coef_rend = cr(notas,cargas_horarias)
print(round(coef_rend,2))
