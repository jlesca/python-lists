# BORRAR ITEMS
# Podemos borrar items de una lista o la lista completa.

# BORRAR UN ITEM
# Mediante el método REMOVE() hacemos mensión al item que deseamos eliminar.

colors = ['red', 'green', 'blue'] # Creo la variable y sus items
print(colors) # Muestro la variable.
colors.remove('green') #Con el metodo remove() indico el item a eliminar.
print(colors) # Muestro mi variable actualizada.


# BORRAR UNA POSICIÓN
# Tambien podemos borrar una posición especifica con el método pop()
# Si no especificamos ninguna posición, Python borrará la úlitma posición de nuestra lista.

colors = ['red', 'green', 'blue'] # Creo la variable y sus items.
print(colors) # Muestro la variable.
colors.pop(1) # Con pop() indico la posición a borrar. En este caso la posición 1 que es 'green'.
print(colors) # Muestro la variable actualizada.


# BORRAR LA LISTA COMPLETA
# Nuestra lista podrá eliminar su contenido con el método CLEAR().

colors.clear() # Limpio el contenido de mi lista.
print(colors) # Muestro la variable actualizada, en este caso vacía y se verá como '[]'.


# ELIMINAR NUESTRA LISTA
# Podremos eliminar completamente nuestra lista con la keyword DEL.

del colors # Elimino la variable.
print(colors) # Muestro la variable, pero en este caso dará error porque ya no existe.
