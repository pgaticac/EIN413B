# 1.	Crear la función vistos_por_ciudad, que recibe como parámetro el nombre del archivo 
# con las observaciones de aves.
# 2.	Leer el archivo con las observaciones.
# 3.	Agrupar las observaciones por ciudad.
# 4.	Ordenar las observaciones de cada ciudad por fecha (de la más antigua a la más nueva).
# 5.	Crear un archivo llamado vistos_por_ciudad.txt con:
#    - El nombre de cada ciudad.
#    - Las fechas y aves observadas en esa ciudad.
# 6.	Retornar cuántas ciudades diferentes aparecen.


def vistos_por_ciudad(archivo):

    observaciones_por_ciudad = {}

    observaciones = open(archivo,"r")
    for linea in observaciones:
        datos = linea.strip().split(":")
        fecha = datos[0]
        ciudad = datos[1]
        aves = datos[2].strip().split(",")
        for ave in aves:
            if ciudad not in observaciones_por_ciudad:
                observaciones_por_ciudad[ciudad]=[]
            observaciones_por_ciudad[ciudad].append([fecha,ave])
            observaciones_por_ciudad[ciudad].sort()

        print(observaciones_por_ciudad)
        #escribir el archivo


    observaciones.close()
    return 0


print(vistos_por_ciudad("observaciones.txt"))
