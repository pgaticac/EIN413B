notas = [55,60,80,75,90]

print(notas)
i = 0

while i < len(notas):
    print("Nota ",i+1,": ", notas[i])
    i+=1
dias = []
semana = ["lunes","martes","miercoles", "jueves","viernes","sabado","domingo"]
print(semana)
finDeSemana = semana[5:]
print(finDeSemana)
dia = list(semana[0])
print(dia)


numeros = list(range(10,101,10))
print(numeros)

miLista = ["uno","tres","cuatro"]
print(miLista)
miLista.append("cinco")
print(miLista)
miLista.insert(1,"dos")
miLista.insert(1,"dos")
print(miLista)
print(miLista.count("seis"))
#print(miLista.index("seis"))
miLista.remove("dos")
miLista.reverse()
print(miLista)
miLista.reverse()
print(miLista)

miLista.sort()
print(miLista)


for numero in miLista:
    print(numero)