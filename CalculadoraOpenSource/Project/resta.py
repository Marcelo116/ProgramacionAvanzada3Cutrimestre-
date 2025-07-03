def restar(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
        print('Error: Debes ingresar solo números válidos. ❌ ')
    
    else:
        resta = int(numero1) - int(numero2)
        print('La resta de tus números es ✅: ', resta)