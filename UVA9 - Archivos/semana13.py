miString = "    hola mundo,\nes lunes; es octubre\n"
#print(miString.strip())
#print("Otra Linea")

#Ejemplo de uso de SPLIT
porDefecto = miString.split()
#print(porDefecto)

porComa = miString.strip().split(",")
#print(porComa)

#Lectura de archivos
archivoPerros = open("perros.txt","r")

for linea in archivoPerros:
    datosPerro = linea.strip().split(";")
    print(datosPerro[1])
    #Acá se procesan los datos como se necesiten

archivoPerros.close()