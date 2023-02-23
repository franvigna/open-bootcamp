def bisiesto(año):
    if año % 4 == 0:
        return "año bisiesto"
    else:
        return "año no bisiesto"
    
print(bisiesto(2023))
print(bisiesto(2024))
