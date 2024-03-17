#Escribe un programa que tome una lista de números enteros como entrada del usuario.
#Luego, convierte cada número en la lista a string y únelos en una sola cadena,
#separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
#de 3 de la cadena final.

lista= []
cant= int(input(print("ingrese la cantidad de elementos que tendra la lista")))
i=0
while i<cant:
     num= int(input(print("ingrese un numero")))
     i+= 1
     lista.append(num)

cadena=""
for letras in lista:
     if letras%3 == 0:
         continue
     else:
         cadena+= str(letras) + "-"
print(cadena)