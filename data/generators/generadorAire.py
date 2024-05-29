import random

def generarDatosCalidadAire():

    listaDatos=[ ]
    for i in range(1000):
        Nombre=random.choice([ 'Manuela Diaz','Juan Salazar','Jimena Jimenez','Jonathan Montes','Mariangel Yepes' ])
        Comuna=random.randint( 1,14 )
        Ica=random.randint( 10,50 )
        Fecha=random.choice([ '20204-05-15','2024-05-16','20204-05-17'])
        Correo=random.choice([ 'correo@correo.com','correo2@correo.com', 'correo3@correo.com','correo4@correo.com', 'correo4@correo.com' ])

        encuesta=[ Nombre, Comuna, Ica, Fecha, Correo]

        listaDatos.append(encuesta)

    return listaDatos
print(generarDatosCalidadAire())
















