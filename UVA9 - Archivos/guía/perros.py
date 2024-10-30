def leer_perros(archivo):
    dicc = {}
    perros = open("C:\\PGC\\EIN413B\\UVA9 - Archivos\\guía\\"+archivo,"r")
    for perro in perros:
        _,n,r,p,s = perro.strip().split(';')

        if n not in dicc:
            dicc[n]=[]
            
        dicc[n].append(s)
    
    perros.close()
    return dicc

def leer_razas(archivo):
    dicc = {}
    perros = open("C:\\PGC\\EIN413B\\UVA9 - Archivos\\guía\\"+archivo,"r")
    for perro in perros:
        _,n,r,p,s = perro.strip().split(';')

        if r not in dicc:
            dicc[r]=[]
            
        dicc[r].append(n)
    
    perros.close()
    return dicc


    

print(leer_perros("perros.txt"))
print(leer_razas("perros.txt"))
#print(mestizos('salchicha','san bernardo','perros.txt'))