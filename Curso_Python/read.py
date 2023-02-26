# numero = 211 
# texto = 'quijote'
# float = 1.5


#print('el numero es {} y el tecto es {} y tiene {}'.format(numero,texto,float))
# print(f'el numero es {numero} y el tecto es {texto} y tiene {float}')

#python string methods   

# f = open(r'C:\Users\Cisco\Desktop\open-bootcamp\Curso_Python\notas.txt')
# datos = f.readlines()
# f.close()
# print(datos)
# r: lectura
# a: append
# w: escritura
# x: create

# t: texto
# b: binario

def main():
    comentarios = listarcomentarios()
    print(comentarios)
    
def listarcomentarios():
    f = open(r'C:\Users\Cisco\Desktop\open-bootcamp\Curso_Python\notas.txt')
    datos = f.readlines()
    f.close()
    
    for linea in datos:
        if linea[0] == '/':
            print(linea)
    
if __name__ == '__main__':
    main()