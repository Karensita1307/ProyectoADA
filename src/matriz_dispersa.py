# disclaimer: muchos comentarios, es costumbre ya.
# creo que eso hace que el código se vea largo, pero ni modo, me sirve

# importa la lista enlazada propia donde se guardan los elementos no nulos
from lista_enlazada import ListaEnlazada

# importa el merge sort propio para ordenar en top_k
from merge_sort import merge_sort_descendente

# clase principal para manejar la matriz dispersa
class MatrizDispersa:

    # metodo constructor de la matriz
    def __init__(self, filas, columnas):

        # guarda la cantidad total de filas de la matriz
        self.filas = filas

        # guarda la cantidad total de columnas de la matriz
        self.columnas = columnas

        # crea la lista enlazada donde se almacenan solo los valores no nulos
        self.datos = ListaEnlazada()

    # obtiene el valor de una posicion
    def get(self, fila, columna):

        # busca el valor en la lista enlazada
        valor = self.datos.buscar(fila, columna)

        # si la posicion no existe, en una matriz dispersa vale 0
        if valor is None:

            # devuelve 0 porque no hay dato guardado en esa celda
            return 0

        # si sí existe, devuelve el valor real
        return valor

    # inserta o actualiza un valor en una posicion
    def set(self, fila, columna, valor):

        # si el nuevo valor es 0, no se debe guardar en una matriz dispersa
        if valor == 0:

            # elimina la posicion si existia
            eliminado = self.datos.eliminar(fila, columna)

            # si se eliminó, la operación fue válida
            if eliminado:

                # devuelve ok para indicar que la operación salió bien
                return "OK"

            # aunque no existiera, igual la celda queda en 0
            return "OK"

        # si el valor no es 0, se inserta o se actualiza
        self.datos.insertar_o_actualizar(fila, columna, valor)

        # devuelve ok porque la operación se completó
        return "OK"

    # elimina el valor de una posicion
    def delete(self, fila, columna):

        # intenta eliminar la posicion en la lista enlazada
        eliminado = self.datos.eliminar(fila, columna)

        # si sí la eliminó
        if eliminado:

            # devuelve ok
            return "OK"

        # si no existia, igual se puede considerar que la celda queda vacia
        return "OK"

    # suma todos los valores de una fila
    def row_sum(self, fila):

        # acumulador para la suma total
        total = 0

        # empieza a recorrer la lista enlazada
        actual = self.datos.head

        # recorre todos los nodos guardados
        while actual is not None:

            # revisa si el nodo pertenece a la fila pedida
            if actual.fila == fila:

                # suma su valor al total
                total += actual.valor

            # avanza al siguiente nodo
            actual = actual.next

        # devuelve la suma final de esa fila
        return total

    # suma todos los valores de una columna
    def col_sum(self, columna):

        # acumulador para la suma total
        total = 0

        # empieza desde la cabeza de la lista
        actual = self.datos.head

        # recorre toda la lista
        while actual is not None:

            # revisa si el nodo pertenece a la columna pedida
            if actual.columna == columna:

                # suma su valor
                total += actual.valor

            # avanza al siguiente nodo
            actual = actual.next

        # devuelve la suma final de esa columna
        return total

    # suma los valores dentro de una region rectangular
    def region_sum(self, fila_inicial, columna_inicial, fila_final, columna_final):

        # acumulador para la suma total
        total = 0

        # empieza desde la cabeza
        actual = self.datos.head

        # recorre todos los nodos almacenados
        while actual is not None:

            # verifica si la fila del nodo está dentro del rango
            dentro_filas = fila_inicial <= actual.fila <= fila_final

            # verifica si la columna del nodo está dentro del rango
            dentro_columnas = columna_inicial <= actual.columna <= columna_final

            # si cumple ambas condiciones, el nodo está dentro de la región
            if dentro_filas and dentro_columnas:

                # suma su valor al total
                total += actual.valor

            # avanza al siguiente nodo
            actual = actual.next

        # devuelve la suma total de la región
        return total

    # intercambia filas por columnas en todos los elementos guardados
    def transpose(self):

        # empieza desde la cabeza de la lista
        actual = self.datos.head

        # recorre todos los nodos
        while actual is not None:

            # guarda temporalmente la fila actual
            fila_temp = actual.fila

            # la nueva fila pasa a ser la columna
            actual.fila = actual.columna

            # la nueva columna pasa a ser la fila original
            actual.columna = fila_temp

            # avanza al siguiente nodo
            actual = actual.next

        # intercambia también las dimensiones generales de la matriz
        temp = self.filas

        # las filas pasan a ser columnas
        self.filas = self.columnas

        # las columnas pasan a ser filas
        self.columnas = temp

        # devuelve ok para confirmar la operación
        return "OK"

    # obtiene los k elementos con mayor valor
    def top_k(self, k):

        # convierte la lista enlazada a una lista normal de tuplas
        elementos = self.datos.a_lista()

        # ordena los elementos de mayor a menor usando merge sort
        elementos_ordenados = merge_sort_descendente(elementos)

        # si k es mayor que la cantidad de elementos, se ajusta
        if k > len(elementos_ordenados):

            # k pasa a ser el tamaño real de la lista
            k = len(elementos_ordenados)

        # devuelve solo los primeros k elementos
        return elementos_ordenados[:k]

    # calcula la densidad de la matriz
    def density(self):

        # obtiene la cantidad de celdas no nulas almacenadas
        no_nulos = self.datos.tamano()

        # calcula cuántas celdas tendría la matriz completa
        total_celdas = self.filas * self.columnas

        # evita división por cero en casos extraños
        if total_celdas == 0:

            # devuelve 0 si la matriz no tiene tamaño válido
            return 0.0

        # devuelve la proporción entre celdas no nulas y total de celdas
        return no_nulos / total_celdas

    # devuelve cuántos elementos no nulos hay guardados
    def cantidad_no_nulos(self):

        # retorna el tamaño actual de la lista enlazada
        return self.datos.tamano()

# resumen de lo que hace toda esa vaina:
# esto convierte nuestra lista enlazada en una matriz dispersa usable, o sea, en vez de guardar una matriz completa gigantesca, solo guarda nodos para las posiciones que tienen valor distinto de cero, que es exactamente la idea del problema 2, yay. 