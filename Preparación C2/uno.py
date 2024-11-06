# Escriba la funcion tienda_mas_cercana(nombre_archivo_tiendas, x, y), que recibe como
# parametro un string con el nombre del archivo que contiene los datos de las tiendas, y dos numeros float con
# las coordenadas donde se encuentra la persona que va a comprar. La funcion debe retornar el nombre de
# la tienda y local mas cercano a esta ubicacion. En caso de empate en el local mas cercano, puede retornar
# cualquiera de los locales cuya distancia es igual.

# ARCHIVOS:
#  1. Abrir archivo
#  2. Recorrer y procesar las líneas
#  3. Cerrar archivo 

import math

def tienda_mas_cercana(archivo,x,y):
    tiendas = open("C:\\PGC\\EIN413B\\Preparación C2\\"+archivo)
    distancia_menor = 1000000000
    for linea in tiendas:
         tienda = linea.strip().split(";")
         nombre_tienda = tienda[0]
         locales = tienda[1].split(":")
         for local in locales:
              infolocal = local.split(",")
              nombre_local = infolocal[0]
              ubix = float(infolocal[1])
              ubiy = float(infolocal[2])
              distancia = math.sqrt((float(x)-ubix)**2 + (float(y)-ubiy)**2)
              #print (nombre_tienda + " " + nombre_local + " " + str(distancia))

              if distancia < distancia_menor:
                   distancia_menor = distancia
                   tienda_cercana = nombre_tienda +" "+nombre_local

    return tienda_cercana

print(tienda_mas_cercana("tiendas.txt",10,5))