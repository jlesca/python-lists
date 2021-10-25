# ORDENAR LISTAS
# Podemos organizar nuestras listas con un orden alfanúmerico de manera ascendente (por defecto) o descendente.
# Esto lo haremos con el método SORT()

print('SORT LIST ASCENDING')
colors = ['red', 'green', 'blue', 'black', 'white', 'pink', 'orange', 'yellow'] # Creo la variable con sus elementos.
colors.sort() # Mediante sort le pido que ordena alfabeticamente los items
print(colors) # Pido que imprima mi nueva lista ahora ordenada
input() # Sale del programa.


# También podemos ordenar elementos de clase int

print('SORT ASCENDING NUMERICALLY')
numbers = [15, 54, 87, 2, 69, 23, 345, 88, 25] # Creo la variable con mi lista de numeros.
numbers.sort() # Le pido que los ordene de manera ascendente.
print(numbers) # Muestro mi variable ahora ordenada. 
input() # Salgo del programa.


# En ambas listas podremos ordenarlo de manera descendente 
# Pero para ello debemos usar el argumento TRUE en la keyword REVERSE.

print('SORT LIST DESCENDING')
numbers = [15, 54, 87, 2, 69, 23, 345, 88, 25] # Creo la variable con mi lista de numeros.
numbers.sort(reverse = True) # Le pido que los ordene de manera ascendente.
print(numbers) # Muestro mi variable ahora ordenada. 
input() # Salgo del programa.


# Python, a su vez, nos permite organizar de manera inversa nuestra lista.

print('REVERSE METHOD')
colors = ['red', 'green', 'blue', 'black', 'white', 'pink', 'orange', 'yellow'] # Creo la variable con sus elementos.
colors.reverse() # Mediante sort le pido que ordena alfabeticamente los items
print(colors) # Pido que imprima mi nueva lista ahora ordenada
input() # Sale del programa.


