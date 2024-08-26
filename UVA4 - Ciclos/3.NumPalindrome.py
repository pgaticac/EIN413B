
num = int(input())

if num < 0 :
    num= num *-1


inv = 0
div = num
#Algoritmo para invertir el numero num
while div != 0:
    mod = div % 10
    div = div // 10 
    inv = inv*10+mod

if num == inv :
    print("El número es palindrome")
else:
    print("El número no es palíndrome")
