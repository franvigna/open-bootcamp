import pickle

class Juguete:
    nombre = ''
    precio = 0.0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def getNombre(self):
        return self.nombre
    
# j1 = Juguete('Potato', 10.5)
# f = open('Curso_Python/datos.bin','wb')
# pickle.dump(j1, f)
# f.close    

f = open('Curso_Python/datos.bin','rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), 'precio: ', potato.precio )

class Estado:
    #players = Players()
    #status = Status()
    life_remaining = 12
    armor = False

#GUARDAR DATOS EN UN FICHERO BINARY
f = open('status.bin','wb')
e = (Estado())
pickle.dump(f, e)
f.close  

#CARGAR DATOS DE UN FICHERO BINARY
f = open('status.bin','rb')
e = pickle.load(f)
f.close()