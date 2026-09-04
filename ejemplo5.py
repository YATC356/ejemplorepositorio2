#MODIFICAR PARA LEER 2 NUMEROS POR TECLADO.
#Y OPERAR: 1=> suma, 2 => resta 3=> multiplicacion
print("CALCULADORA \nIngresa 2 números")
numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))
print ("selecciona operacion: 1=> suma, 2=> resta, 3=> multiplicacion")
opcion= int(input("selecciona operacion: "))
match opcion:
    case 1:
        print(f"SUMA")
        print(f"Resultado: {numero1 + numero2}")
    case 2:
        print(f"RESTA")
        print(f"Resultado: {numero1 - numero2}")
    case 4:
        print(f"MULTIPLICACION")
        print(f"Resultado: {numero1 * numero2}")
    case 5:
        print(f"")
    case _:
        print(f"Ninguna opcion {opcion}")