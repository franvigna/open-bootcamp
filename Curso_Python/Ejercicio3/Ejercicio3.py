peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))

imc = peso / (altura ** 2)
imc_rounded = round(imc, 2)

print(f"Tu indice de masa corporal es {imc_rounded}.")