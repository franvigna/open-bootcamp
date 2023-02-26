lista = [
    'una linea',
    'dos lineas',
    'tres linear'
]



def escribe(fichero, datos):
    f = open('Curso_Python/mifichero.txt', 'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea += '\n'
        f.write(linea)
    f.close

escribe('mifichero.txt', lista)
