#  0       1     2         3        4           5          6  
#nombre;region;comuna;dependencia;rural;latitud;longitud;matricula

zona = {
    "0" : "rural",
    "1" : "urbano"
}


def establecimientos_x_region(nombre_archivo, tipo):
    establecimientos_file = open("C:\\PGC\\EIN413B\\Preparación C2\\2023-2\\"+nombre_archivo,encoding="utf8")
    establecimientos = list()
    salida = list()
    regiones = {}
    e_tipo=""
    for e in establecimientos_file:
        e_tipo = (e.strip().split(";"))[4]
        if e_tipo == str(tipo) :
            establecimientos.append(e.strip().split(";"))

    #establecimientos filtrados por tipo
    for e in establecimientos:
        region = e[1]
        if region not in regiones:
            regiones[region] = list()
        regiones[region].append(e)    


    #establecimientos filtrados por región        
    for region in regiones:
        exregion = open("C:\\PGC\\EIN413B\\Preparación C2\\2023-2\\"+region +"_"+zona[e_tipo] +".txt", "w")
        for e in regiones[region]:
            #print(e)
            exregion.write("{0} ({1}): {2} estudiantes\n".format(e[0],e[2],e[7]))
        exregion.close()
    return 0



print(establecimientos_x_region("establecimientos.csv", 1))