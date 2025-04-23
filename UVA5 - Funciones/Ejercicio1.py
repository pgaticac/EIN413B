def saludar(nombre):
    mensaje = "¡Hola, " + nombre + "!"
    return mensaje


nombre = input("Como te llamas?: ")
saludo = saludar(nombre)
print(saludo)
