import random
estudiantes = ["Bruno","Pedro","Antonio","Clara","Rita"]
notas = list()
c = 0

while c < 5:
    notas.append(random.randint(0,100))
    c+=1
print(estudiantes)
print(notas)
min = max = notas[0]
prom = 0
for nota in notas:
    if nota > max:
        max = nota
    
    if nota < min:
        min = nota
       
    prom += nota

prom = prom / len(notas)

print("Promedio de Notas: ", prom)
print("Nota Maxima: ", max," ", estudiantes[notas.index(max)])
print("Nota Mínima: ", min," ", estudiantes[notas.index(min)])