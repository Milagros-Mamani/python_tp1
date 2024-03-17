#Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
#con los número pares y otras con los que son impares. Imprima las listas al terminar de
#procesarlas.

#CODIGO EJERCICIO 4
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in lista:
      if num %2 == 0:
           print(num)

listaPar= []
listaImp= []

for num in lista:
      if num %2== 0:
           listaPar.append(num)
      else:
           listaImp.append(num)

print("acontinuacion se imprimira la lista de numeros pares")
for num in listaPar:
      print(num)
 
print("acontinuacion se imprimira la lista de numeros impares")
for num in listaImp:
      print(num)