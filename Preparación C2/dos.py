# Escriba la funci  ́on analizar_productos(nombre_archivo_tiendas)), que recibe como par  ́ame-
# tro un string con el nombre del archivo que contiene los datos de las tiendas.
# La funci  ́on debe crear un archivo para cada producto encontrado, cuyo nombre debe construirse con el
# nombre del producto agregando el sufijo .txt. Ese archivo debe contener los nombres de las tiendas que
# venden el producto, una por l ́ınea, incluyendo el precio de venta. Los productos deben aparecer en orden
# creciente (de menor a mayor) seg  ́un el precio. Adem  ́as, en la  ́ultima l ́ınea el archivo debe contener el valor
# promedio del producto, considerando todas las tiendas que lo venden. Deben considerarse  ́unicamente
# productos con stock positivo. Para el formato de los archivos, gu ́ıese por los ejemplos.
# Adem  ́as de crear los archivos, la funci  ́on debe retornar el n  ́umero de archivos que fueron cread

def analizar_productos(archivo):
    tiendas = open("C:\\PGC\\EIN413B\\Preparación C2\\"+archivo)
    for linea in tiendas:
         tienda = linea.strip().split(";")
         nombre_tienda = tienda[0]
         nombre_archivo = nombre_tienda+".txt"

         bodega_tienda = open("C:\\PGC\\EIN413B\\Preparación C2\\"+nombre_archivo)

         for producto in bodega_tienda:
              print(producto.strip())
        
    return 0


print(analizar_productos("tiendas.txt"))