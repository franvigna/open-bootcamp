#class es una clase
#las variables dentro de una clase se llaman propiedades
#las funciones dentro de una clase se llaman metodos
"""
class Juguete:
    _encendido = True

    def __init__(self):
        print('estoy en la clase juguete soy el constructor')
    #para modificar una propiedad de clase se utiliza self.
    def apaga(self):
        self._encendido = False
    
    def enciende(self):
        self._encendido = True

    def isEncendido(self):
        return self._encendido

#crear una instancia es crear un objeto
#cada instancia es independiente
d1 = Juguete()
d1.apaga()
print(d1.isEncendido())

d2 = Juguete()
d2.enciende()
print(d2.isEncendido())

class Dino(Juguete):
    color = None
    nombre = None
    
    #declaracion de contructor
    def __init__(self):
        super().__init__()
        print('estoy en el contructor de la clase dino') 
    def __del__(self):
        print('estoy en el destructor de la clase',self.__class__)    
    
    def verEscamas(self):
        pass

    
  
p = Dino()
print(p.color)
print(p.nombre)
#llamar a destructor
# del(p)

"""

#composicion

class Categorias:
    IdCategoria = 0
    Nombre = ''
    
class Proveedores:
    idProveedor = 0
    nombre =- ''

class Productos:
    idProduct = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoDeProducto = 0
    CIFproveedor = Proveedores()
    
p = Productos()
p.CIFproveedor.nombre
p.CategoriaProducto.IdCategoria

