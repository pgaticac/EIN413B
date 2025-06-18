
def tamaño_aves(nombre_archivo):
    archivo = open(nombre_archivo,"r")
    aves = {
        "Grande":[],
        "Mediana":[],
        "Pequeña":[]
    }

    for linea in archivo:
        lista = linea.strip().split(";")
        tamaño_prom = lista[4].split("-")
        T = (int(tamaño_prom[0])+int(tamaño_prom[1]))/2
        id = lista[0]
        nivel = lista[5]

        if T < 25 :
            clasificacion = "Pequeña"
        elif T < 55 :
            clasificacion = "Mediana"
        else:
            clasificacion = "Grande"
        
        aves[clasificacion].append([T,id,nivel])

    archivo.close()
    for tamaño in aves:
        aves[tamaño].sort()
    
    return aves



aves = tamaño_aves("info.csv")
print(aves["Pequeña"])