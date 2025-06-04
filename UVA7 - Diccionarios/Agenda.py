agenda = []

# contacto = {
#     "nombre":"Bruno",
#     "apellido":"Diaz",
#     "edad": 45,
#     "ciudad":"Gótica",
#     "carrera":"Seguridad",
#     "email":['bdiaz@usm.cl','batman@gmail.com'], 
# }

#agenda.append(contacto)

def nuevoContacto():
    res = True

    contacto = {}
    contacto["nombre"] = input("Nombre: ")
    contacto["apellido"] = input("Apellido: ")
    contacto["edad"] = input("Edad: ")
    contacto["ciudad"] = input("Ciudad: ")
    contacto["carrera"] = input("Carrera: ")
    contacto["email"] = []
    
    while(res==1):
        contacto["email"].append(input("Email:"))
        res = int(input("Quieres ingresar otro email? 1:Si 0:No"))

    return contacto



def imprimirAgenda(agenda):
    print("\n\nAGENDA")
    if len(agenda) != 0:
        for contacto in agenda:
            print()
            for key in contacto:
                if key != "email":
                    print(f"{key:10}: {contacto[key]}")
                else:
                    for e in contacto["email"]:
                        print(f"{'email':10}: {e}")
    else:
        print("No hay contactos en la agenda")            



res = 1
while(res == 1):
    contacto = nuevoContacto()
    agenda.append(contacto)
    imprimirAgenda(agenda)
    res = int(input("Quieres agregar otro contacto? 1:Si 0:No"))

