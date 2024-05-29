import random
def generarParticulasPm():
    listaDatosParticulasPm=[ ]
    for i in range(1000):
        Estacion=random.randint( 1,36 )
        EstadoAlerta=random.choice([ 'Buena', 'Moderada', 'Dañina para grupos sensibles', 'Dañina para la salud', 'Muy dañina a la salud', 'Sin datos en las ultimas 24 horas', 'No aplicanormatividad'])
        CantidadParticulasPm10=random.randint(15,60)
        CantidadParticulasPm2_5=random.randint(5,30)
        Fecha=random.choice([ '20204-05-24','2024-05-25','20204-05-26'])
        Ubicacion=random.choice(['Estación Poblado', 'Estación Belén', 'Estación Buenos Aires', 'Estación La Alpujarra', 'Estación Universidad de Antioquia', 'Estación Itagüí', 'Estación Sabaneta', 'Estación Bello' ])
        Temperatura=random.choice([ '20°C', '21°C', '22°C', '23°C', '24°C', '25°C', '26°C', '27°C', '28°C', '29°C', '30°C', '31°C', '32°C',])

        encuesta= [Estacion, EstadoAlerta, CantidadParticulasPm10, CantidadParticulasPm2_5, Fecha, Ubicacion, Temperatura]
        listaDatosParticulasPm.append(encuesta)
    return listaDatosParticulasPm
print(generarParticulasPm())
