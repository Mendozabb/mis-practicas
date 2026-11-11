class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None #REFERENCIA QUE INDICA EL ORIGEN DE LA LISTA
    def insertar_final(self,dato):
        nuevo_nodo=Nodo(dato)

        #Caso 1: si la ista esta vacia, eol nuevo nodo se va a convertir en la cabeza
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
            return

        #caso 2: recorrer hasta el ultimo elemento o nodo existente
        actual=self.cabeza
        while actual.siguiente is not None:
            actual=actual.siguiente
        #Conectar el ultimo nodo con el nuevo nodo
        actual.siguiente=nuevo_nodo
    def mostrar_lista(self):
                actual=self.cabeza
                elementos=[]
                while actual is not None:
                    elementos.append(str(actual.dato))
                    actual=actual.siguiente
                print("---".join(elementos)+"..None")

#uso del programa
lista=ListaEnlazada()

#Insertar elementos
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")

#Mostramos el resultado
lista.mostrar_lista()
        