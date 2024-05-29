import random
def generarResiduosSolidos():
    listaDatosResiduosSolidos=[ ]
    for u in range(1000):
        Comuna=random.randint( 1,14 )
        CantidadToneladas=random.randint( 1,100 )
        Estado=random.choice(['Precario', 'Aceptable', 'Buen estado', 'Optimas condiciones' ])
        Fecha=random.choice([ '20204-05-27','2024-05-28','20204-05-29'])
        Dirección=random.choice([ 'cll 105 #88e- 2','', 'Calle 70 # 49-06','Carrera 80 # 4A-94', 'Calle 59 # 77-13', 'Carrera 65 # 44-81' ])
        PeriocidadRecoleccionDias=random.randint( 1,4 )

        encuesta= [Comuna, CantidadToneladas, Estado, Dirección, Fecha, PeriocidadRecoleccionDias]
        listaDatosResiduosSolidos.append(encuesta)
    return listaDatosResiduosSolidos
print(generarResiduosSolidos())