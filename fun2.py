#REESCRIBIENDO
#FUNCION PROCEDIMENTAL: NO DEVUELVE RESULTADOS , 
#Solo ejecuta una tarea.
def detectarTemperatura(lectura,consigna):

    if lectura == consigna:
        #Acciones si es verdadero.
        print(f"La temperatura es igual a {consigna}")
        lectura = lectura + 3
        print(f"temperatura: {lectura}")

    else:
        #Acciones si es falso
        print(f"La Temperatura no es igual a {consigna}")
        lectura = lectura - 1
        print(f"temperatura: {lectura}")

detectarTemperatura(10,17)
detectarTemperatura(30,29)
detectarTemperatura(17,14)
detectarTemperatura(22,-4)
