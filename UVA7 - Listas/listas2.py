#Copiado de listas por referencia y valor
listaA = list()
listaB = list()

listaA.append("Uno")
listaB.append("Rojo")

#listaA=listaB         # copia de  referencia
listaA=listaB.copy()   # copia de valores

print(listaA)
print(listaB)

listaB.append("Verde")

print(listaA)
print(listaB)

#Listas de Listas

estudiantes = [["E1", [100,80,55]],
               ["E2" ,[80,85,90]],
               ["E3", [90,90,90]]
               ]

for estudiante in estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1]
    promedio = 0
    for nota in notas:
        promedio+=nota
    promedio=promedio/len(notas)
    print(nombre, " promedio: ", promedio)
