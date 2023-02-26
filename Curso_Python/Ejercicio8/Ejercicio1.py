file = open('Curso_Python/Ejercicio8/texto.txt', 'w')
file.write('¡He creado mi primer archivo!\n')
file.close()

file = open('Curso_Python/Ejercicio8/texto.txt', 'r+')
file.readline()
file.write('Esta es la segunda vez que escribo.\n')
file.close()

file = open('Curso_Python/Ejercicio8/texto.txt', 'r+')
file.readline()
file.write('Esta es la tercera vez que escribo.\n')

file.seek(0)
print(file.read())
file.close()