def es_divisible(a, b):
   if a%b==0:
      #print(True)
      return True
   else:
      #print(False)
      return False

a = 5
b = 10
if es_divisible(b, a):
   print(b, "es divisible por", a)
else:
   print(b, "no es divisible por", a)
