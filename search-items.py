# BUSCAR ITEMS EN UNA LISTA
# Podemos buscar si exite un item específico en nuestra lista haciendo uso de un IF y la keyword IN.
# Vamos a crear un buscador de artículos de PC para un usuario.


art = ['laptop', 'computer', 'mouse', 'keyboard', 'display'] # Creo la variable con los items.
search = input("Ingrese el artículo que desea buscar: ") # Creo una variable de busqueda. Mediante input el usuario podrá ingresar el texto.

# Se almacenará el texto ingresado en la variable 'search'

if search in art: # Si el contenido de la variable 'search', existe en el contenido de la variable 'art', que haga lo siguiente:
  print ('El artículo existe') # Mostrará este mensaje.
else: # Si no existe, que haga lo siguiente:
  print ('El artículo no existe') # Mostrará este otro mensaje.

input() # Sale del programa.
