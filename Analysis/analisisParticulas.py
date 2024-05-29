import pandas as pd 

from data.generators.generadorParticula import generarParticulasPm

def construirPariculasDataFrame():
    datosParticulas=generarParticulasPm()

    particulasDataFrame=pd.DataFrame(datosParticulas, colums=[ 'Estacion', 'Estado Alerta', 'Cantidad Particulas Pm 10', 'Cantidad Particulas Pm 2.5', 'Fecha', 'Ubicacion', 'Temperatura' ])

    print(particulasDataFrame)

construirPariculasDataFrame()