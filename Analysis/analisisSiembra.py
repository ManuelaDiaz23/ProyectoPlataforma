import pandas as pd 

from data.generators.generadorSiembra import generarSiembraArboles

def contruirSiembraDataFrame():
    datosSiembra=generarSiembraArboles()

    siembraDataframe=pd.DataFrame(datosSiembra,columns=['Corregimineto', 'Hectareas Sembradas', 'Especies Sembradas', 'Nombres', 'Fecha', 'Correo' ])

    print(siembraDataframe)

contruirSiembraDataFrame()