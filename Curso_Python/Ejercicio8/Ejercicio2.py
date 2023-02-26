import pickle

class Vehiculo:
    ruedas = 0
    color = ''
    puertas = 0
    
    def __init__(self, ruedas, color, puertas):
        self.ruedas = ruedas
        self.color = color
        self.puertas = puertas
    
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas, self.puertas )
        
    
v1 = Vehiculo(4, 'rojo', 2)
f = open('Curso_Python/Ejercicio8/Vehiculo.bin','wb')
pickle.dump(v1, f)
f.close()    

f = open('Curso_Python/Ejercicio8/Vehiculo.bin','rb')
potato = pickle.load(f)
f.close()