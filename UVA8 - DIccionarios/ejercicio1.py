series = [ 
['Game of thrones','USA',9.4,['ficcion']], 
['24','USA',8.4,['accion','suspenso']], 
['La casa de papel','España',9.2,['accion','suspenso','drama']], 
['Orange is the new black', 'USA', 8.5, ['comedia','drama']], 
['Dark', 'Alemania', 9.2, ['ficcion','drama']], 
['Sherlock','UK',9.2,['policial','drama','suspenso']], 
['Merl ́ı','Espa ̃na',9.5,['drama']], 
['Whitecollar','USA',8.2,['comedia','drama','suspenso']], 
['Heroes','USA',7.7,['ficcion','accion']], 
['Mistfit','UK',8.4,['accion','drama','ficcion']] 
]

def series_x_genero(series):
    generos={}

    for serie in series:
        generosSerie = serie[3]
        for genero in generosSerie:
            if genero not in generos:
                generos[genero] = list()
            
            generos[genero].append(serie[0])

        generos[genero].sort()
    return generos

print(series_x_genero(series))