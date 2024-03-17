#Implementa un programa que solicite al usuario que ingrese una lista de números.
#Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
#Nota: utilice la sentencia break cuando haga falta

lista= []
cant= int(input(print("ingrese la cantidad de elemntos de la lista")))
i=0
while i<cant:
     i+=1
     num= int(input(print("ingrese un numero")))
     lista.append(num)

print("lista generada")

for num in (lista):
     if num<0:
         print("se imgreso un numero negativo, se cortara el programa")
         break
     else:
         print(num)