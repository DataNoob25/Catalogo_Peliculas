import os
class CatalogosPeliculas:
 ruta_archivo="Pelicula.txt"

 @classmethod
 def agregar_pelicula(cls,pelicula):
     with open(cls.ruta_archivo,"a",encoding="utf8") as archivo:
        archivo.write(f"{pelicula.nombre}\n")
 @classmethod
 def listar_peliculas(cls):
     with open(cls.ruta_archivo,"r",encoding="utf8") as archivo:
         print("Catalogo de peliculas".center(50,"-"))
         print(archivo.read())

 
 def eliminar_peliculas(cls):
     os.remove(cls.ruta_archivo)
     print("Archivo eliminado: {}".format(cls.ruta_archivo))

class Pelicula:
    def __init__(self,nombre):
        self._nombre=nombre

    def __str__(self):
        return " Pelicula: {}".format(self._nombre) 
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre








while opcion !=4:
     try:
       print("opciones: ")
       print("1. Agregar Pelicula")
       print("2. Listar Peliculas")
       print("3. Eliminar Catalogo Peliculas")
       print("4. Salir")
       opcion=int(input("Escribe tu opcion(1-4): "))

       if opcion == 1:
         nombre=input("proporcione el nombre de la pelicula: ")
         pelicula=Pelicula(nombre)
         CatalogosPeliculas.agregar_pelicula(pelicula)
      
       elif opcion == 2:
         CatalogosPeliculas.listar_peliculas()
       elif opcion==3:
        CatalogosPeliculas.eliminar_peliculas()

     except Exception as e:
      print("Ocurrio un error", e)
      opcion=None

else:
    print("Salimos del programa")







