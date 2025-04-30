#Crea una función esPrimo() que reciba un número y retorne True 
# si el número es primo.
#Ejemplo: esPrimo(7) debería retornar True.

def esMultiplo(n1,n2):
    mod = n1%n2

    if mod == 0 :
        return True
    else:
        return False

def esPrimo(numero):
    for i in range(2,numero):
       if esMultiplo(numero,i):
           return False
    
    return True
       


print(esPrimo(11))