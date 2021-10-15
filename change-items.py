# CAMBIAR ITEMS DE UNA LISTA
# Podemos cambiar el valor de un item de nuestra lista haciendo referencia a su posición.

colors = ['red', 'green', 'blue'] # Creo la variable con sus items.
print(colors) # Muestro su contenido
colors[1] = 'yellow' # Accedo a la posición 1 y modifico el contenido. En este caso será 'green' por 'yellow'
print(colors) # Muestro de nuevo el contenido de mi variable.


# También podemos acceder a un rango para poder cambiar su contenido.

colors = ['red', 'green', 'blue', 'black', 'white'] # Creo la variable y sus items
print(colors) # Muestro su contenido.
colors[1:3] = ['yellow', 'violet'] # Accedo al rango de la posición 1 hasta la 3. Python no incluye la última. Modificara 'green' y 'blue'
print(colors) # Muestro de nuevo su contenido.


# INSERTAR UN ITEM
# Podemos insertar un item en nuestra lista mediante el método INSERT()

colors = ['red', 'green', 'blue'] # Creo la variable y sus items.
print(colors) # Muestro su contenido.
colors.insert(2, 'yellow') # Inserto en la posición 2 el item 'yellow'. El resto de los items se correrán una posición hacia la derecha.
print(colors) # Muestro su nuevo contenido.
