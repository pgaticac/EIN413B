contactos = list()
contacto = {}

contacto["nombre"]="juan"
contacto["telefono"] = 333333
contacto["email"] = "juan@usm.cl"

contactos.append(contacto)

contacto={}

contacto["nombre"]="clara"
contacto["telefono"] = 222222
contacto["email"] = "clara@usm.cl"
contactos.append(contacto)

#print(contacto)
#print(contactos)

print("Ingresa el nombre del contacto: ", end="")
nombre = input()

print("Buscando información de",nombre)
existe = False
for contacto in contactos:
    if contacto["nombre"] == nombre:
        print("Telefono: ", contacto["telefono"])
        existe = True

if existe == False :
    print("Contacto no existe")


