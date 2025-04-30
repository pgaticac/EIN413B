#Crea una función contarVocales() 
# que reciba una cadena de texto y retorne cuántas vocales tiene.
#Ejemplo: contar_vocales("Python es genial") debería retornar 5.

def contarVocales(cadena):
    cont = 0
    for letra in cadena:
        if letra in 'aeiouAEIOU':
            cont = cont + 1   #cont+=1
    
    return cont

print(contarVocales("Python es genial"))
print(contarVocales("SDF"))
print(contarVocales("1-.,"))
print(contarVocales("Aula"))