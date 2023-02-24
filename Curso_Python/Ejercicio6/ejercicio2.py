class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
        
    def resultado(self):
        if self.nota < 7:
            print('El alumno ha suspendido')
        else:
            print('El alumno ha aprobado')
            
alum1=Alumno()
alum2=Alumno()

alum1.inicializar('Ivana', 7)
alum2.inicializar('Francisco', 4)

alum1.imprimir()
alum1.resultado()
alum2.imprimir()
alum2.resultado()
