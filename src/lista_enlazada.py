# esta es la clase para representar un nodo de la lista enlazada
# disclaimer: muchos comentarios! (es mi manera de estudio)
class Nodo:

    # metodo constructor del nodo
    def __init__(self, fila, columna, valor):

        # guarda la fila de la celda
        self.fila = fila

        # guarda la columna de la celda
        self.columna = columna

        # guarda el valor de la celda
        self.valor = valor

        # apunta al siguiente nodo de la lista
        self.next = None


# clase para manejar la lista enlazada simple
class ListaEnlazada:

    # metodo constructor de la lista
    def __init__(self):

        # referencia al primer nodo de la lista
        self.head = None

        # guarda cuántos nodos hay en la lista
        self._size = 0

    # inserta un nuevo nodo o actualiza uno existente
    def insertar_o_actualizar(self, fila, columna, valor):

        # empieza a recorrer desde el primer nodo
        actual = self.head

        # recorre toda la lista buscando la posicion
        while actual is not None:

            # verifica si la posicion ya existe
            if actual.fila == fila and actual.columna == columna:

                # actualiza el valor si ya existe
                actual.valor = valor

                # avisa que no se insertó, sino que se actualizó
                return "actualizado"

            # avanza al siguiente nodo
            actual = actual.next

        # crea un nodo nuevo si la posicion no existia
        nuevo = Nodo(fila, columna, valor)

        # el nuevo nodo apunta al actual primero
        nuevo.next = self.head

        # ahora el nuevo nodo pasa a ser la cabeza
        self.head = nuevo

        # aumenta el tamaño de la lista
        self._size += 1

        # avisa que se insertó un nuevo nodo
        return "insertado"

    # busca el valor de una posicion
    def buscar(self, fila, columna):

        # empieza desde el primer nodo
        actual = self.head

        # recorre la lista
        while actual is not None:

            # revisa si encontro la posicion
            if actual.fila == fila and actual.columna == columna:

                # devuelve el valor encontrado
                return actual.valor

            # avanza al siguiente nodo
            actual = actual.next

        # devuelve none si la posicion no existe
        return None

    # elimina un nodo por fila y columna
    def eliminar(self, fila, columna):

        # empieza desde el primer nodo
        actual = self.head

        # guarda el nodo anterior para poder reconectar la lista
        anterior = None

        # recorre toda la lista
        while actual is not None:

            # revisa si este es el nodo que se quiere borrar
            if actual.fila == fila and actual.columna == columna:

                # si no hay anterior, el nodo a borrar es la cabeza
                if anterior is None:

                    # mueve la cabeza al siguiente nodo
                    self.head = actual.next

                # si hay anterior, se salta el nodo actual
                else:

                    # conecta el nodo anterior con el siguiente del actual
                    anterior.next = actual.next

                # disminuye el tamaño de la lista
                self._size -= 1

                # avisa que sí se eliminó
                return True

            # guarda el nodo actual como anterior
            anterior = actual

            # avanza al siguiente nodo
            actual = actual.next

        # avisa que no encontró el nodo a eliminar
        return False

    # convierte la lista enlazada a una lista normal de tuplas
    def a_lista(self):

        # crea una lista vacia para guardar los datos
        datos = []

        # empieza desde la cabeza
        actual = self.head

        # recorre toda la lista
        while actual is not None:

            # agrega la informacion del nodo en forma de tupla
            datos.append((actual.fila, actual.columna, actual.valor))

            # avanza al siguiente nodo
            actual = actual.next

        # devuelve la lista final
        return datos

    # devuelve el tamaño actual de la lista
    def tamano(self):

        # retorna la cantidad de nodos guardados
        return self._size

    # elimina todos los nodos de la lista
    def vaciar(self):

        # quita la referencia al primer nodo
        self.head = None

        # reinicia el tamaño de la lista
        self._size = 0