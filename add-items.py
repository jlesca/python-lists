# AGREGAR ITEMS A NUESTRA LISTA
# Ademas de poder modificar nuestra variable,reemplazando un item por otro, podemos agregar elementos a ella.
# Veremos los métodos APPEND (), INSERT () y EXTEND().


# APPEND()
# Con este método podemos agregar items a nuestra lista, y este se posicionará siempre al final de ella.

colors = ['red', 'green', 'blue'] # Creo la variable y asignos sus items.
print(colors) # Muestro la variable
colors.append('yellow') # Mediante appendn() agrego un item más a mi lista original 'colors'
print(colors) # Muestro el valor actualizado de mi variable.


# INSERT()
# Mediante este método podremos añadir un elemento a nuestra lista, pero especificando su posición.

colors.insert(1, 'black') # Para hacer uso de insert, debemos marcar la posición, en este caso 1, y el nuevo item a añadir en esa posición.
print(colors) # Muestro mi variable actualizada. Los items se moverán una posición a la derecha.


# EXTEND()
# Con este método podemos extender nuestra lista con los items de otra lista.

colors = ['red', 'green', 'blue'] # Creo la variable con sus items.
new_colors = ['yellow', 'violet', 'orange'] # Creo una nueva variable con los items a agregar,.
colors.extend (new_colors) # Mediante extend añado al final de mi lista 'colors' los items de 'new colors'.
print(colors # Muestro la variable actualizada.
      
