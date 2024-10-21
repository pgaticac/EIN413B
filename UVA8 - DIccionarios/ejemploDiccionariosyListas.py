contactos = list()
contacto = {}

contacto["nombre"]="juan"
contacto["telefono"] = 333333
contacto["email"] = "juan@usm.cl"

contactos.append(contacto)

print(contacto)
print(contactos)

contacto={}

contacto["nombre"]="clara"
contacto["telefono"] = 222222
contacto["email"] = "clara@usm.cl"
contactos.append(contacto)

print(contacto)
print(contactos)


print(contactos[0]["telefono"])