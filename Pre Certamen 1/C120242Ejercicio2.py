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



print(comer("5042132", "3D5;5I2;4D1;2D9;9I3", 2))
print(comer("111111", "1D2;1D2;1D2;1D2;1D2;5I2", 0))