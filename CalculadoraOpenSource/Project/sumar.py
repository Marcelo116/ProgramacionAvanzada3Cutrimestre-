def sumar(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
     print('Error: Debes ingresar solo números válidos. ❌ ')
   
    else:
        suma = int(numero1) + int( numero2)
        print('La suma de tus números es ✅: ', suma)
     