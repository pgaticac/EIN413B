# 1.	Crear la función mas_vistos, que recibe como parámetro el nombre del archivo con 
# las observaciones de aves.
# 2.	Contar cuántas veces aparece cada tipo de ave.
# 3.	Crear un archivo llamado mas_vistos.txt que contenga las 3 aves más vistas, 
# desde la que más se repite hasta la que menos.
# 4.	Retornar la cantidad de aves que se observaron.

def mas_vistos(archivo):

    observaciones = open(archivo,"r")

    avistamientos ={}

    for o in observaciones:
        datos = o.strip().split(":")
        aves = datos[2].strip().split(",")
        for ave in aves:
            if ave not in avistamientos:
                avistamientos[ave]=0

            avistamientos[ave]+=1

        
    observaciones.close()

    aves_ordenadas = []

    for ave in avistamientos:
        aves_ordenadas.append([avistamientos[ave],ave])
    
    aves_ordenadas.sort()
    aves_ordenadas.reverse()
    
    archivo = open("mas_vistos.txt","w")

    for datos in aves_ordenadas[:3]:
        archivo.write(f"Se observaron {datos[0]} especimenes de {datos[1]}\n")

    archivo.close()

    return len(aves_ordenadas)


print(mas_vistos("observaciones.txt"))
