#Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
#luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

temperatura= int(input(print("ingrese una temperatura en grados celsius")))
g_fahrenheit= int(temperatura * (int (9/5)) + 32)
print (f'{g_fahrenheit} ºF es el resultado de convertir {temperatura} ºC a grados Fahrenheit')