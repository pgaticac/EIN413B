print("Factorial de un Número")
print("Ingresa un número para calcular su factorial: ", end="")
num = int(input())

i = 1
factorial = 1

while i <= num :
    factorial = factorial * i
    i = i + 1

print(num,"! = ", factorial)