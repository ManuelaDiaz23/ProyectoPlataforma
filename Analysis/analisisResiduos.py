import pandas as pd 

from data.generators.generadorResiduos import generarResiduosSolidos

def contruirResiduosDataFrame():
    datosResiduos=generarResiduosSolidos()

    residuosDataFrame=pd.DataFrame(datosResiduos, columns=[ 'Comuna', 'Cantidad en Toneladas', 'Estado', 'Fecha', 'Dirección', 'Periocidad Recolección'])
    
    print(residuosDataFrame)

contruirResiduosDataFrame()