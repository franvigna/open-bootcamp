# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def mifuncion(x):
#     if x % 2 == 0:
#         return True
    
#     return False

# #FILTER
# resultado = filter(lambda x: x % 2 == 0, numeros)

# print(list(resultado))

#MAP
#resultado = map(FUNCION, LISTA)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def cuadrado(x):
#     return x * x

# resultado = map(lambda x: x * x, numeros)

# print(list(resultado))


#REDUCE
# from functools import reduce
# #reduce(FUNCION, LISTA)
# def suma(a, b):
#     return a + b

# resultado = reduce( suma, [1, 2, 3, 4, 5])

# print(resultado)

#ZIP asocia los elements de una lista con los elementos de otra
# cursos = ['Java', 'Python', 'Git']
# asistentes = [15, 20, 25]
# demo = zip(cursos, asistentes)
# print(list(demo))

#all() ALL sirve para verificar que todos los elementos de una lista se cumplan
#any() ANY sirve para verificar que algun elemento de la lista cumpla una condicion

# listaA = [1 == 1, 2 == 2, 2 == 3]

# #any = or or or or or
# res1 = any(listaA)
# print(res1)

# #all = and and and and
# res2 = all(listaA)
# print(res2)

#ROUND REDONDEA HACIA ARRIBA SI SUPERA .5
# nums = [3.5, 4.8, 1.1]
# res1 = map(round, nums)

# print(list(res1))

# #devuelve el valor menor de la lista
# print(min(nums))

# #pow POTENCIA = 2**5
# print(pow(2,5))

# lista = ['z','c','h','t','a']
# #ORDENAR
# ordenada = sorted(lista)

# #ORDENAR AL REVES
# alreves = sorted(lista, reverse = True)

# print(ordenada)
# print(alreves)

# from getpass import getpass

# user = input('Username: ')
# pas = getpass('Password: ', )

# print(f'tu usuario es {user} y tu contraseña es {pas}')




