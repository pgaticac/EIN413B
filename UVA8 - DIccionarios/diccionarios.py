agenda = {'juan':123456789, 
          'pedro':234567891, 
          'maria':345678912}


#agenda = {}
print(agenda)

#agregar elemento
agenda['clara']=333333

print(agenda)

#modificar un elemento que ya existe
agenda['juan'] = 222222
print(agenda)

#eliminar el nodo del diccionario (completo llave y valor)
del agenda['maria']
print(agenda)

#consulta del contenido de un elemento del diccionario
print(agenda['clara'])

#cantidad de elementos en el diccionario
print(len(agenda))

#Responde True si la llave existe en el diccionario sino responde False
print('clara' in agenda)

#recorrer diccionario
for llave in agenda:
    print(llave, ": ", agenda[llave])