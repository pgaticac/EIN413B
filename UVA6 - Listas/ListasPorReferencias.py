def agregar(lista,valor):
    lista.append(valor)


lista1 = []
lista1.append("uno")
lista1.append("dos")

print(lista1)
agregar(lista1.copy(),"tres")
print(lista1)
