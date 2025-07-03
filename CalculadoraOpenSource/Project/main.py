from CalculadoraOpenSource.Project.dividir import dividir
from CalculadoraOpenSource.Project.multiplicacion import multiplicar
from CalculadoraOpenSource.Project.suma_avanzada import suma_multiples_numeros
from CalculadoraOpenSource.Project.sumar import sumar
from CalculadoraOpenSource.Project.resta import restar
while True:
    print()
    print('Hola, bienvenido a Calculadora Open source')
    print('Presiona 1 para realizar una suma de dos numeros')
    print('Presiona 2 para realizar una resta de dos numeros')
    print('Presiona 3 para realizar una multiplicacion de dos numeros')
    print('Presiona 4 para realizar una division de dos numeros')
    print('Presiona 5 para realizar una suma de n numeros')
    print('Presiona 6 para salir')
    print()
    accion = input('¿Qué deseas hacer? ')
    accion = accion.lower()
    print()
    if accion == '1':
        print('*** Suma de dos números ***')
        numero1 = input('Por favor, ingresa el primer número: ')
        numero2 = input('Por favor, ingresa el segundo número: ')
        sumar(numero1, numero2)
    elif accion == '2':
        print('*** Resta de dos números ***')
        numero1 = input('Por favor, ingresa el primer número: ')
        numero2 = input('Por favor, ingresa el segundo número: ')
        restar(numero1, numero2)
        
    elif accion == '3':
        print('*** Multiplicación de dos números ***')
        numero1 = input('Por favor, ingresa el primer número: ')
        numero2 = input('Por favor, ingresa el segundo número: ')
        multiplicar(numero1, numero2)
        
    elif accion == '4':
        print('*** División de dos números ***')
        numero1 = input('Por favor, ingresa el primer número: ')
        numero2 = input('Por favor, ingresa el segundo número: ')
        dividir(numero1, numero2)
        
    elif accion == '5':
        print('*** Suma de n números ***')
        suma_multiples_numeros()
    elif accion == '6':
        print('*** Salir ***')
        break
    else:
        print('Lo siento, esa no es una acción válida. Por favor, intenta nuevamente.')