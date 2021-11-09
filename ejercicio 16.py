
from heap import HeapMax

cola = HeapMax()


#a cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
cola.arribo("empleado 1",2)
cola.arribo("empleado 2",2)
cola.arribo("empleado 3",2)


#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print("El primero de la cola es: ")
print(cola.atencion())
print()

#c. cargue dos documentos del staff de TI.
cola.arribo("staff-TI 1",2)
cola.arribo("staff-TI 2",2)

#d. cargue un documento del gerente.
cola.arribo("gerente 1",3)

#e. imprima los dos primeros documentos de la cola.
print("los dos primeros de la cola son: ")
print(cola.atencion())
print(cola.atencion())
print()

#f. cargue dos documentos de empleados y uno de gerente.
cola.arribo("gerente 2 ",3)
cola.arribo("empleado 4",1)
cola.arribo("empleado 5",1)


#g. imprima todos los documentos de la cola de impresión.
while(not cola.vacio()):
    print(cola.atencion())