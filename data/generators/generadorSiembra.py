import random
def generarSiembraArboles():
    listaDatosSiembra=[ ]
    for i in range(1000):
        Corregimineto=random.randint( 1,9 )
        HectareasSembradas=random.randint( 1,200 )
        EspecieSembradas=random.choice([ 'Roble', 'Ceiba', 'Pino', 'Eucalipto', 'Caoba', 'Palma de coco', 'Arce', 'Sauce', 'Alamo', 'Cedro'])
        Nombre=random.choice([ 'Maria Pestana','Leidy Angel','Mariana Urrea','Juan Montañez','Angelica Londoño' ])
        Fecha=random.choice([ '20204-05-21','2024-05-22','20204-05-23'])
        Correo=random.choice([ 'correo66@correo.com','correo26@correo.com', 'correo36@correo.com','correo46@correo.com', 'correo56@correo.com' ])

        encuesta= [ Fecha, Corregimineto, HectareasSembradas, EspecieSembradas, Nombre, Correo]
        listaDatosSiembra.append(encuesta)
    return listaDatosSiembra
print(generarSiembraArboles())