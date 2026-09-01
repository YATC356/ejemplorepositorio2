#BLOQUE IF
temperatura = 17
if temperatura == 17:
    #Acciones si es verdadero.
    print("Es verdad, estoy dentro de la estructura de control IF")
    temperatura = temperatura + 3
    print(f"temperatura: {temperatura}")

else:
    #Acciones si es falso
    print("Tambien estoy dentro de la estructura")
    temperatura = temperatura - 1
    print(f"temperatura: {temperatura}")

print("Estoy fuera de la estructura IF")
temperatura = temperatura * 10
print(f"temperatura: {temperatura}")


