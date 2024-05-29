import pandas as pd 

from data.generators.generadorRuido import generarRuidoAmbiental

def construirRuidoDataFrame():
    datosRuido=generarRuidoAmbiental()

    ruidoDataFrame=pd.DataFrame(datosRuido,columns=['Comuna', 'Direccion', 'Nombre', 'Decibelios Diurnos', 'DecibelosNocturnos', 'Fecha' ])

    print(ruidoDataFrame)

construirRuidoDataFrame()