def dividir(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
        print('Error: Debes ingresar solo números válidos. ❌ ')
    if (int(numero2) == 0):
        print('❌ Error: No se puede dividir entre cero')
    
    else:
        division = int(numero1) / int(numero2)
        print('La división de tus números es ✅: ', division)