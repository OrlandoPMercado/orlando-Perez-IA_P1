#el programa primero usa un bucle while para llenar una lista de numeros y despues utiliza un ciclo for y condicionale para determinar si los numeros son par o impar
print("En este programa se muestra la solucion a los preoblemas de los capitulos del 20-30\n")

lista = []
z=0
 
x=0

while x <= 100:
    lista.append (x)
    x += 1
    
print (lista)
    
    

for y in range(10):
   # print(lista[y])
    z = lista[y]
    if z % 2 == 0:
       print("el numero es par")
      
    else:
        print("es impar")
        # print("es impar.")

     