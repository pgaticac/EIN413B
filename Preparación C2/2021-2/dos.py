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
  tiendas = open("C:\\PGC\\EIN413B\\Preparación C2\\2021-2\\"+archivo)
  productos = {}
  cont_archivos = 0

  for linea in tiendas:
    tienda = linea.strip().split(";")
    nombre_tienda = tienda[0]
    archivo_tienda = nombre_tienda + ".txt"

    archivo_productos_tienda = open("C:\\PGC\\EIN413B\\Preparación C2\\2021-2\\"+archivo_tienda)
    for linea_producto in archivo_productos_tienda:
      producto = linea_producto.strip().split(";")
      if int(producto[2]) > 0:
        if producto[0] not in productos:
          productos[producto[0]] = list()

        producto_tienda = {}
        producto_tienda["tienda"] = nombre_tienda
        producto_tienda["precio"] = producto[1]
        productos[producto[0]].append(producto_tienda)
    archivo_productos_tienda.close()

  
  for producto in productos:
    promedio = 0
    lista_precios = productos[producto]
    archivo_producto = open("C:\\PGC\\EIN413B\\Preparación C2\\2021-2\\"+producto + ".txt", "w")
    cont_archivos+=1
    for precio in lista_precios:
      archivo_producto.write("{0} : ${1}\n".format(precio["tienda"],precio["precio"]))
      promedio+=int(precio["precio"])

    promedio = promedio/len(lista_precios)
    archivo_producto.write("Precio promedio para {0} : ${1}".format(producto,promedio))
  return cont_archivos


print(analizar_productos("tiendas.txt"))
