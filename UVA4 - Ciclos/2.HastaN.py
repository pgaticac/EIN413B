valido = False
while valido == False:
    print("n= ",end="")
    n = int(input())

    #validación
    if n >= 1:
        valido = True
    else:
        print("Error. N debe ser mayor o igual a 1")

cont = 1
while cont <= n:
    print(cont, end=" ")
    cont+=1


