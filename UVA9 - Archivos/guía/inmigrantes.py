def filtrar(archivo,año):
    dicc = {}
    inmigrantes = open("C:\\PGC\\EIN413B\\UVA9 - Archivos\\guía\\"+archivo,"r")
    for inmigrante in inmigrantes:
        datos = inmigrante.strip().split(":")
        fecha = datos[3]
        pais = datos[2]
        nombre = datos[1]
        añoIngreso = (fecha.split("-"))[2]
        if int(añoIngreso) == año:
            if pais not in dicc:
                dicc[pais] = []
            
            dicc[pais].append(nombre)

    inmigrantes.close()
    return dicc


def contar_ingresos(archivo,año):
    dicc = {}
    inmigrantes = open("C:\\PGC\\EIN413B\\UVA9 - Archivos\\guía\\"+archivo,"r")
    for inmigrante in inmigrantes:
        datos = inmigrante.strip().split(":")
        fecha = datos[3]
        pais = datos[2]
        añoIngreso = int((fecha.split("-"))[2])
        if int(añoIngreso) == año:
            if pais not in dicc:
                    dicc[pais] = 0
            dicc[pais]+=1
    inmigrantes.close()
    return dicc
        

print(filtrar("inmigrantes.txt",2019))
print(contar_ingresos("inmigrantes.txt",2019))
print(contar_ingresos("inmigrantes.txt",2018))
