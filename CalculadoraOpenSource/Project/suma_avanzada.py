def suma_multiples_numeros():
    suma = 0
    contador = 1
    
    while True:
        entrada = input(f"Ingrese el número #{contador}: ")
        
        if entrada.strip().lstrip('-').isdigit():
            suma += int(entrada)
            contador += 1
            
            continuar = input("¿Quieres ingresar otro número? (s/n): ").strip().lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Respuesta inválida. Escribe 's' para sí o 'n' para no ❌.")
            if continuar == 'n':
                break
    
    print(" La suma total es✅ :", suma)
