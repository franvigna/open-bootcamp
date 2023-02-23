

# > mayor
# >= mayor igual
# == exactamente igual
# <= menor igual
# < menor
"""
a = 5
b = 6
resultado = a > b

print(resultado)
if a == 6:
  print('el numero es 5')
else:
  print('es otro numero')
  
contador = 0

while contador <= 10:
  contador += 1

  if contador % 2 == 0:
    print(contador, " es un numero par")
    continue
 

contador = 0

while contador <= 10:
  print("contador vale ",contador)

  if contador == 5:
    break
  
  contador += 1
"""


# for valorActual in lista:
#   print(valorActual)
  #print(type(valorActual))

# longitud = len(lista)
# print('la lista tiene',longitud)

# for numero in range(longitud):
#   print(lista[numero])

# for palabra in lista:
#   print('palabra actual: ', palabra)
  
#   if palabra == 'mensaje':
#     print('he encontado la palabra mensaje')
#     break

# if "masaje" not in lista:
#   print('no hay masaje')

# lista = [3,4,1,2,5]
# print(lista)

# listaOrdenada = sorted(lista)
# print(listaOrdenada)
# listaOrdenadaReves = sorted(lista, reverse = True)
# print(listaOrdenadaReves)

# letras = ['a','B','z','Y','o','P','b']
# letrasOrdenadas = sorted(letras)
# print(letrasOrdenadas)


# valor = 3
# match valor:
#   case 1:
#     print('valor es 1')
#   case 2:
#     print('valor es 2')
#   case 3:
#     print('valor es 3')
#   case 4:
#     print('valor es 4')
#   case 5:
#     print('valor es 5')

lista = ['hola','mensaje','adios']

for palabra in lista:
  if palabra == 'mensaje':
    print('encuentro la palabra mensaje')
    break 
else:
  print('no encuentro nada')
