import random
def generarRuidoAmbiental():
    listaDatosRuido=[ ]
    for i in range(1000):
        Comuna=random.randint( 1,14 )
        Direccion=random.choice([ 'cll 103 #82e- 23','', 'Calle 10 # 45-56','Carrera 80 # 34A-14', 'Calle 50 # 75-30', 'Carrera 65 # 49-85' ])
        Nombre=random.choice([ 'Maria Diaz','Jaime Salazar','Jimena Urrea','Juana Montes','Angel Yepes' ])
        DecibeliosDiurnos=random.randint( 10,47 )
        DecibelosNocturnos=random.randint( 10,35)
        Fecha=random.choice([ '20204-05-18','2024-05-19','20204-05-20'])

        encuesta=[ Nombre, Comuna, Fecha, Direccion, DecibeliosDiurnos, DecibelosNocturnos]

        listaDatosRuido.append(encuesta)
    return listaDatosRuido
print(generarRuidoAmbiental())