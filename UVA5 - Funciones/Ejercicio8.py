#Crea una función esMultiplo() que reciba dos números 
# y retorne True si el primero es múltiplo del segundo.
#Ejemplo: es_multiplo(15, 5) debería retornar True.

def esMultiplo(n1,n2):
    mod = n1%n2

    if mod == 0 :
        return True
    else:
        return False
    


print(esMultiplo(15,5))
print(esMultiplo(13,5))      

