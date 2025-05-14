lista_invitados = []

def confirmar(invitado):
    esta = lista_invitados.count(invitado)
    if esta == 1:
        indice = lista_invitados.index(invitado)
        lista_invitados[indice] = lista_invitados[indice].upper()

lista_invitados.append("Bruno")
lista_invitados.append("Pedro")
lista_invitados.append("Antonio")

print(lista_invitados)
confirmar("Bruno")
print(lista_invitados)