print("Ingresa coordenadas del centro del círculo:")
print("X=", end="")
centroX = int(input())
print("Y=", end="")
centroY = int(input())
print("El centro del círculo se ubica en  (", centroX , "," , centroY ,")")

print("Ingresa el radio del círculo:")
print("r=",end="")
r = int(input())

print("Ingresa coordenadas a evaluar: ")
print("X=", end="")
cX = int(input())
print("Y=", end="")
cY = int(input())

#límites del círculo estan en centroX +/- r y centroY +/- r

#evaluando Eje X
if cX > centroX + r  or cX < centroX - r:
    print("Punto fuera del círculo")
else:
    print("Evaluando coordenada Y")

