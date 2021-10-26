# SORT CASE SENSITIVE
# Por defecto Python ordena primero las palabras con su primer letra mayuscula y luego las que no.
# Sin importar el orden del abecedario. Esto lo llamamos CASE SENSITIVE.

print('CASE SENSITIVE') # Muestro el título
colors = ['red', 'Green', 'blue', 'White', 'black', 'Yellow'] # Creo la var y sus items
print(colors) # Muestro la var
colors.sort() # Ordeno los items de manera ascendente 
print(colors) # Muestro la var actualizada


# SORT CASE INSENSITIVE
# Por suerte podemos desactivar esto mediante el uso de una función clave STR.LOWER dentro del método SORT
# De esta manera Python ordenara sin importar el uso de mayúscula en algunas palabras.

print('CASE INSENSITIVE') # Muestro el título
colors = ['red', 'Green', 'blue', 'White', 'black', 'Yellow'] # Creo la var y sus items
print(colors) # Muestro la var
colors.sort(key = str.lower) # Ordeno los items de manera ascendente 
print(colors) # Muestro la var actualizada

input() # Salgo del programa con ENTER
