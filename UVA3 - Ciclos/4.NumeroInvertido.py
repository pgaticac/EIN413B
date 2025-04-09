print("Ingresa un número: ",end="")
num = int(input())

#Algoritmo para invertir el numero num
inv = 0
div = num

while div != 0:
    mod = div % 10
    div = div // 10 
    inv = inv*10+mod

print(num , "//" , inv)