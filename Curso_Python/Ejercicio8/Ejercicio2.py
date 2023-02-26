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
        return f"Color {self.color}, {self.ruedas} ruedas, {self.puertas} puertas"
    
    
GolTrend = Vehiculo(4, 'rojo', 2)

print(GolTrend)

file = open('Curso_Python/Ejercicio8/Vehiculo.bin','w+b')

pickle.dump(GolTrend, file)

file.seek(0)    

NuevoGolTrend = pickle.load(file)

print(NuevoGolTrend)

file.close()
