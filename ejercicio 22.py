#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

#F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.
from cola import Cola

class Personajes (object):
    def __init__ (self, nombre_personaje, nombre_superheroe,genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

cola_personajes = Cola()

personaje = Personajes("Tony Stark", "Iron Man", "M")
cola_personajes.arribo(personaje)
personaje = Personajes("Steve Rogers", "Capitan America", "M")
cola_personajes.arribo(personaje)
personaje = Personajes("Natasha Romanoff", "Black Widow", "F")
cola_personajes.arribo(personaje)
personaje = Personajes("Carol Danvers", "Capitana Marvel", "F")
cola_personajes.arribo(personaje)
personaje = Personajes("Scott Lang", "Ant-Man", "M")
cola_personajes.arribo(personaje)

cantidad_elementos = 0
cont_femenino = ''
cont_masculino = ''

while(cantidad_elementos < cola_personajes.tamanio()):
    dato = cola_personajes.mover_al_final()
    #Punto A
    if (dato.nombre_superheroe == 'Capitana Marvel' ):
        print('El nombre de personaje de la superheroe ',dato.nombre_superheroe,' es ',dato.nombre_personaje)

    if (dato.genero == 'F'): 
        cont_femenino +=(' ' +dato.nombre_personaje)
        
    if (dato.genero == 'M'):
        cont_masculino += (' ' + dato.nombre_personaje)
        
    #Punto E
    if (dato.nombre_personaje[0] == 'S'):
        print('El personaje que empieza con S es ',dato.nombre_personaje)
    if (dato.nombre_superheroe[0] == 'S'):
        print('El superheroe que empieza con S es ',dato.nombre_superheroe)

    #Punto D
    if (dato.nombre_personaje == 'Scott Lang' ):
        print('El nombre de super heroe del personaje ',dato.nombre_personaje,' es ',dato.nombre_superheroe)

     #Punto F
    if (dato.nombre_personaje == 'Carol Danvers' ):
        print('El personaje  ',dato.nombre_personaje,' se encuentra en la cola y su nombre de superheroe es ',dato.nombre_superheroe)


    cantidad_elementos  += 1

print(' nombres femeninos: ', cont_femenino) 
print(' nombres masculinos : ', cont_masculino) 
