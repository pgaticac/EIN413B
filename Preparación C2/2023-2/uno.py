#  0       1     2         3        4      5       6        7  
#nombre;region;comuna;dependencia;rural;latitud;longitud;matricula

from math import sin, cos, sqrt, atan2, radians

def mas_cercanos(nombre_archivo, latitud, longitud):
    establecimientos_file = open("C:\\PGC\\EIN413B\\Preparación C2\\2023-2\\"+nombre_archivo,encoding="utf8")
    establecimientos = list()
    for linea in establecimientos_file :
        establecimiento = linea.strip().split(";")
        e_nombre = establecimiento[0]
        if establecimiento[5] != "SIN INFO" and establecimiento[6]!= "SIN INFO":
            e_distancia = distancia(latitud,longitud,float(establecimiento[5]), float(establecimiento[6]))
            if e_distancia <= 1:
                e = [e_distancia,e_nombre,dependencia(establecimiento[3])]
                establecimientos.append(e)
        
    establecimientos.sort()

    salida = list()
    for establecimiento in establecimientos:
        salida.append([establecimiento[1],establecimiento[2]])
    return salida

def distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0
    # Convierte las latitudes y longitudes de grados a radianes
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    # Diferencia en coordenadas
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Fórmula de Haversine
    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    # Distancia en kilómetros
    dist = R * c
    return dist

def dependencia(codigo):
    if codigo == "1": return "MUNI"
    if codigo == "2": return "SUBV"
    if codigo == "3": return "PAGA"
    if codigo == "4": return "CAD"
    if codigo == "5": return "SLE"
    return "ERROR"




print(mas_cercanos("establecimientos.csv", -33.4918, -70.6175))
