
dic1 = {  #en esta parte estamos creando un diccionario
    "perro": "negrro",
    "gato" : "siames",
    "pajaro": "colibri"
 
    }

for x in dic1:#usamos un bucle for 
    print(x)#con este comando imprimimos el diccionario

def Diccionario(): #aqui realizamos una funcion para copiar un diccionario
       dic2= dic1.copy()#con esto hacemos una copia del diccionario
       dic1.clear()#con esto eliminimaos el diccionario original
       print(dic2)
       
       
Diccionario()#aqui llamamos a la funcion

class alum:#creamos clase alumn
    def__init_(self,nombre,edaad): #usamos constructores
         self.nombre = nombre #le creams variables
         self.edad = edaad 
     
     def muestra_datos(self):#le agregamos funciones
     print("El nombre y edad del alimno son:" + self.nombre, self.edad)
     
alum1 = alum("enrique", 22)#creamos una instancia
alum1.muestra_datos()#llamamos a la funcion para que nos muestre los datos
    














