#Crea una función llamada areaCirculo()
#que reciba el radio de un círculo y retorne su área.
#Usa π = 3.14159.

def areaCirculo(r):
    area = 3.14159 * (r**2)
    return area


radio = int(input("Radio="))
area = areaCirculo(radio)
print(area)
