from cola import Cola

class Personajes (object):
    def __init__ (self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta


cola_personajes = Cola()
cola_aux = Cola()

personaje = Personajes('Jar Jar Binks','Alderaan')
cola_personajes.arribo(personaje)
personaje = Personajes('Han Solo','Endor')
cola_personajes.arribo(personaje)
personaje = Personajes('Luke Skywalker','Marte')
cola_personajes.arribo(personaje)
personaje = Personajes('Yoda','Tatooine')
cola_personajes.arribo(personaje)

cantidad_elementos = 0

while(cantidad_elementos < cola_personajes.tamanio()):
    dato = cola_personajes.mover_al_final()
    #Punto A
    if (dato.planeta == 'Alderaan'):
        print('El personaje del planeta ',dato.planeta,' es ',dato.nombre)
    if (dato.planeta == 'Tatooine'):
        print('El personaje del planeta ',dato.planeta,' es ',dato.nombre)
    if (dato.planeta == 'Endor'):
        print('El personaje del planeta ',dato.planeta,' es ',dato.nombre)
    
    #Punto B
    if (dato.nombre == 'Luke Skywalker'):
        print('El planeta natal del personaje',dato.nombre,' es ',dato.planeta)
    if (dato.nombre == 'Han Solo'):
        print('El planeta natal del personaje',dato.nombre,' es ',dato.planeta)

    cantidad_elementos  += 1

#Punto C
while (not cola_personajes.cola_vacia()):
    dato = cola_personajes.atencion()

    if (dato.nombre == 'Yoda'):
        personaje = Personajes('Obi','Marte')
        cola_aux.arribo(personaje)
        cola_aux.arribo(dato)
    else:
        cola_aux.arribo(dato)    

while (not cola_aux.cola_vacia()):
    cola_personajes.arribo(cola_aux.atencion())   

print('La cola agregando el nuevo personaje antes de Yoda')
cantidad_elementos = 0
while(cantidad_elementos < cola_personajes.tamanio()):
     dato = cola_personajes.mover_al_final()
     print(dato.nombre)
     cantidad_elementos += 1


#Punto D
cont = 0

while (cont < cola_personajes.tamanio()):
    dato = cola_personajes.atencion()

    if (dato.nombre == 'Jar Jar Binks'):
        cola_aux.arribo(dato) #lo guarda
        cont += 1
        dato2 = cola_personajes.atencion() #lo saca y no lo guarda
    else:
        cola_aux.arribo(dato) 
        cont += 1 

while (not cola_aux.cola_vacia()):
    cola_personajes.arribo(cola_aux.atencion())   

print('La cola eliminando el personaje siguiente a Jar Jar binks')
cantidad_elementos = 0
while(cantidad_elementos < cola_personajes.tamanio()):
     dato = cola_personajes.mover_al_final()
     print(dato.nombre)
     cantidad_elementos += 1


