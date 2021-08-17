#Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
#nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
#ni métodos de ordenamiento.

from cola import Cola

valores1 = [1,2,3,4,5]
valores2 = [6,7,8,9,10]

cola1 = Cola()
cola2 = Cola()

for i in valores1:
    cola1.arribo(i)

for i in valores2:
    cola2.arribo(i)


cant = 0 

while(cant < cola1.tamanio()):
     dato = cola1.mover_al_final()
     cant += 1
while(not cola2.cola_vacia()):
     dato = cola2.atencion()
     cola1.arribo(dato)
     


cant = 0
print('ambas colas ordenadas en cola numero 1')
while(cant < cola1.tamanio()):
     dato = cola1.mover_al_final()
     print(dato)
     cant += 1
