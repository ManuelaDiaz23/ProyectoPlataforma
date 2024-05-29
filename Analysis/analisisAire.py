import pandas as pd

from data.generators.generadorAire import generarDatosCalidadAire

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()

    #generamos el dataframe
    aireDataFrame=pd.DataFrame(datosAire,columns=['Nombre', 'Comuna', 'Ica', 'Fecha', 'Correo' ])

    print(aireDataFrame)

construirAireDataFrame()















