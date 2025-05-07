# [40 %] Escriba un programa que solicite inicialmente el plan de comidas y la ingesta mínima de alimento que
# debe satisfacer el picaflor. Posteriormente, debe solicitar la cantidad de plantaciones que serán analizadas.
# Para cada una de las plantaciones se debe pedir la configuración de las flores e indicar si cumple o no conla ingesta mínima.
# Al finalizar, se debe mostrar cuál es la plantación que permitiría obtener la mayor cantidad de alimento al
# picaflor. En caso de que haya empate en el mayor, puede mostrar cualquiera de los que empatan. 

# Ingrese el plan de comida: 3D5;5I2;4D1;2D9;9I3
# Ingrese la ingesta mínima para el día: 11
# Ingrese el número de plantaciones a analizar: 3
# Plantación 1
# Ingrese la plantación: 5042132
# Ingrese la casilla de inicio: 2
# Cumple! Come 11
# Plantación 2
# Ingrese la plantación: 1111111111
# Ingrese la casilla de inicio: 0
# No cumple con la ingesta m ́ınima, apenas come 4
# Plantación 3
# Ingrese la plantación: 6271438001
# Ingrese la casilla de inicio: 1
# Cumple! Come 17
# La plantación 3 es la que permite comer más

def comer(plantacion,plan,inicio):
    flores = 0
    i = 0
    pos = inicio
    while(i<len(plan)):
        paso =  plan[i:i+3]
        mov  =  int(paso[0])
        dire =  paso[1]
        come =  int(paso[2])
        
        #Si dire es D sumo mov a pos.
        if(dire == "D"):
            pos = pos + mov
        #Si me paso, pos es len(plantacion)-1
            if(pos >= len(plantacion)):
                pos = len(plantacion)-1
        #Si dire es I resto mov a pos.
        else:
            pos = pos - mov
            #Si me paso, pos es 0
            if(pos < 0):
                pos = 0

        #COME
        hay = int(plantacion[pos])
        if (hay >= come):
            hay = hay - come
            flores += come
        else:
            flores += hay
            hay = 0

        #ACTUALIZAR PLANTACION
        plantacion = plantacion[:pos] + str(hay) + plantacion[pos+1:]
               
        i+=4
    return flores


def main():
    # plan = input("Ingrese el plan de comida: ")
    # ingesta = int(input("Ingrese la ingesta mínima para el día: "))
    # plantaciones = int(input("Ingrese el número de plantaciones a analizar: "))
    
    plan = ""
    ingesta = 0
    plantaciones = 0

    plantacion_max = 0
    max_flores = 0

    for i in range(plantaciones):
        print(f"Plantación {i+1}")
        plantacion = input("Ingrese la plantación: ")
        inicio = int(input("Ingrese la casilla de inicio: "))
        
        # Llamar a la función comer para calcular la cantidad de flores que puede comer el picaflor
        flores_comidas = comer(plantacion, plan, inicio)
        
        if flores_comidas >= ingesta:
            print(f"Cumple! Come {flores_comidas}")
            plantacion_max = i + 1
            max_flores = flores_comidas
            if flores_comidas > max_flores:
                plantacion_max = i + 1
                max_flores = flores_comidas
        else:
            print(f"No cumple con la ingesta mínima, apenas come {flores_comidas}")

    print(f"La plantación {plantacion_max} es la que permite comer más")
    print(f"Cantidad de flores comidas: {max_flores}")

main()