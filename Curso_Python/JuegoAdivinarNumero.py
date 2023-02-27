secreto = 50
valor = 0
while valor != secreto:
    valor = int(input('Adivina que numero estoy pensando: '))
    
    if valor > secreto:
        print('Muy Alto')
        continue
    if valor < secreto:
        print('muy bajo')
        continue
    
    if valor == secreto:
        print('¡GANASTEEE!')