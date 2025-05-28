import random

# estudiantes = ["Bruno","Pedro","Antonio","Clara","Rita"]
curso = [["Bruno"],["Pedro"],["Antonio"],["Clara"],["Rita"]]

for e in curso:
    e.append(random.randint(0,100))

print(curso)

prom = 0
max = ["",-1]
min = ["",101]

for e in curso:
    nota = int(e[1])

    prom = prom + nota

    if nota > max[1]:
        max[1] = nota
        max[0] = e[0]
    if nota < min[1]:
        min[1] = nota
        min[0] = e[0]

prom = prom / len(curso)
print("Prom: ", prom)
print("Max: ", max)
print("Min: ", min)