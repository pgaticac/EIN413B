tope = int(input())

i = 1
cuadrado = 1

while cuadrado < tope :
    cuadrado = i * i
    i = i+1

    if cuadrado < tope:
         print(cuadrado)