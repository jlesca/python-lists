# SIN LISTA DE COMPRENSION
# Con Python podemos crear una una nueva lista basada en los elementos de otra lista.
# El programa creará a partir de una lista llamada 'colors', otra lista llamada 'new_colors' con todos los elementos 
# que contengan la lentra 'e' y los mostrará en pantalla.

print('WITH OUT LIST COMPREHENSION') # Muestro título
colors = ['red', 'green', 'blue', 'yellow', 'black', 'white', 'brown'] # Creo la variable y asigno sus elementos
print(colors) # Muestro la variable de ejemplo
new_colors = [] # Creo una variable vacía donde se irá creando una lista con los resultados de los colores con letra 'e'.

for item in colors: # Creo la variable 'item' que tomara como valor cada elemento de la variable 'colors'.
  if 'e' in item: # Si el valor de 'e'' está incluido en la variable 'item', haga lo siguiente.
    new_colors.append(item) # Agregue a la variable 'new_colors' los valores tomados por la var 'item'
    
print('SHOW ME COLORS WITH E') # Muestro el título.
print(new_colors) # Muestro los resultados de la búsqueda.
input() # Salgo del programa.python


# CON LISTA DE COMPRENSION
# En Python podemos escribir lo mismo pero en una sola línea.

print('WITH LIST COMPREHENSION')
colors = ['red', 'green', 'blue', 'yellow', 'black', 'white', 'brown'] # Creo la variable y asigno sus elementos.
print(colors) # Muestro la variable de ejemplo
new_colors = [item for item in colors if 'e' in item] # Creo una variable donde irá creando una lista con los resultados de los colores con letra 'e'.
print('SHOW ME COLORS WITH E') # Muestro el título.
print(new_colors) # Muestro los resultados de la búsqueda.
input() # Salgo del programa.
