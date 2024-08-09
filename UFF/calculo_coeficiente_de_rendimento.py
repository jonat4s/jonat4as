""" Aqui como calcular o CR ( coeficiente de rendimento ) para alunos da UFF, utilizando dados aleatórios como exemplo """

# Insira as notas das disciplinas ( abaixo como converter string em float para facilitar)

notas = ["8,4", "8,5", "3,0", "7,0", "4,2", "10,0", "6,5", "7,7", "8,3", "8,0", "6,5", "7,3", "10,0", "10,0",
         "10,0", "7,5", "9,1", "8,9", "10,0", "7,1", "9,3", "10,0", "8,0", "6,0", "7,7", "7,6", "7,0", "6,5",
         "10,0", "7,3", "6,5", "6,3", "6,6", "6,9", "9,0", "8,3", "8,6", "5,6", "6,4", "8,7", "8,8", "9,1"]

# Converter para float
notas_float = [float(nota.replace(",", ".")) for nota in notas]

# Insira a carga horária com números float

carga_horaria = [72.0,72.0,60.0,60.0,60.0,60.0,60.0,72.0,72.0,60.0,72.0,60.0,72.0,72.0,60.0,68.0,72.0,72.0,72.0,60.0,72.0,60.0,
72.0,72.0,72.0,30.0,60.0,30.0,72.0,60.0,68.0,60.0,68.0,30.0,72.0,72.0,60.0,60.0,72.0,72.0,72.0,72.0]


# Função que calcula o CR a partir dos dados dispostos

def cr(notas, carga_horaria):

    return sum(x * y for x, y in zip(notas, carga_horaria)) / sum(carga_horaria)


# Chamando a função e calculando o CR arredondando a média.
coef_rend = cr(notas_float,carga_horaria)
print(round(coef_rend,2))
