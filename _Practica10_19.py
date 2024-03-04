print("En este programa se dara solucion a los problemas del cap 10-19.\n")
print("")

lista= ["kant", "foucault", "nietzsche" , "rousseau"]#en esta linea creo una lista
del lista[-1]# en esta linea elimino un miembro de la lista seleccionandolo con numeros negativos
lista.remove("kant")#aqui removimos un miembro de la lista pero esta vez con la funcion "remove"
destructor = lista.pop(1)#en esta linea sacamos un elemnto de la lista para guardarlo en otra variable.
lista.append("marx")
lista.insert(-1, "engels")#en esta linea agregamos otro miembro a la lista pero esta vez le pudimos asignar un lugar gracias a la funcion "insert
lista.sort()#con la funcion "sort" organizamos alfabeticamente los miembros de la lista.

print ("\nel ultimo elmento eliminido fue:\t" + destructor)#imprimimos el valor eliminado que rescatamos.
print ("\nel numero todal de elemntos en la lista son:" )
print ( len(lista))#con la funcion len podemos  saber el numero de elemntos en una lista


tupla = tuple(lista)#aqui convertimos la lista en una tuple

print (tupla)
print("\n")

print (tupla[0], tupla[3])# en esta linea estamos imprimiendo la dupla demostrando la diferencia con las listas.

print("\n")
