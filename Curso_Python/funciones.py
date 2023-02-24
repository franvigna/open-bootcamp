# temperatura= 12.6

# def mifuncion(a='francisco'):
#     global temperatura
#     temperatura = 5.0
#     print('tu nombre es', a ,'la temperatura es de ',temperatura )

# mifuncion('juan') #llamado a la funcion


# def matematicas(a=0,b=0,c=0):
#     def suma(a=0,b=0,c=0):
#         resultadoSuma = a + b + c
#         print(resultadoSuma)
#     def resta(a=0,b=0,c=0):
#         resultadoResta = a - b - c
#         print(resultadoResta)        
#     suma(a,b,c)  
#     resta(a,b,c)   
    
# matematicas(5,7,3)
# matematicas(1)
# matematicas(c=6)
# matematicas()


# def operaciones(a,b):
#     return a + b, a-b , a*b , a/b
# suma, resta, multi, divi = operaciones(2, 4 )
# print(suma)
# print(resta)
# print(multi)
# print(divi)


# def sumador(**kwargs):
#     inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
#     final = kwargs['final'] if 'final' in kwargs else 0
    
#     resultado=0
#     for x in range(inicial,final +1):
#         resultado += x
        
#     return resultado

# res=sumador(final=3)
# print(res)
    
anonima = lambda nombre, apellido: print('hola', nombre, apellido)
anonima('juan','perez')

sumatoria = lambda x: x+x
print(sumatoria(50))
