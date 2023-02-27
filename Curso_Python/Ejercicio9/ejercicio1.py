text = input('Dame una lista de paises(separado por comas)')

paises = text.split(', ')

paises = set(paises)

paises = sorted(paises)

print(list(paises))

