from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

pares = filter(lambda x: x % 2 == 0, lista)

print(list(pares))

resultado = reduce( lambda a, b: a + b, pares)

print(resultado)
