import msvcrt

porcentaje = 0
while porcentaje < 100:
    porcentaje += 25 #incrementar en 25 a la variable
    print(f"Cargando... {porcentaje}%")
print("Descarga completa!")

#implementar un bucle que se detenga 
#cuando la tecla pulsada es "ESC"

print("Bucle en marcha... Presiona la tecla ESC para detenerlo.")

while True:
    print("Procesando datos...")  # Aquí va tu código interno
    
    # Comprueba si el usuario tocó una tecla
    if msvcrt.kbhit():
        # Lee la tecla pulsada y verifica si es ESC (código hexadecimal \x1b)
        if msvcrt.getch() == b'\x1b':
            print("\n¡Tecla ESC detectada! Saliendo del bucle de forma segura.")
            break