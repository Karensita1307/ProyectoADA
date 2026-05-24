# nuestro merge sort. disclaimer: muchos comentarios again

# ordena una lista de tuplas por valor de mayor a menor
def merge_sort_descendente(datos):

    # caso base: si hay 0 o 1 elementos, ya está ordenado
    if len(datos) <= 1:

        # devuelve la misma lista
        return datos

    # calcula la mitad de la lista
    medio = len(datos) // 2

    # toma la parte izquierda
    izquierda = datos[:medio]

    # toma la parte derecha
    derecha = datos[medio:]

    # ordena recursivamente la mitad izquierda
    izquierda_ordenada = merge_sort_descendente(izquierda)

    # ordena recursivamente la mitad derecha
    derecha_ordenada = merge_sort_descendente(derecha)

    # mezcla ambas mitades ya ordenadas
    return mezclar_descendente(izquierda_ordenada, derecha_ordenada)


# mezcla dos listas ya ordenadas de mayor a menor
def mezclar_descendente(izquierda, derecha):

    # lista donde se guardará el resultado final
    resultado = []

    # índice para recorrer la izquierda
    i = 0

    # índice para recorrer la derecha
    j = 0

    # compara elementos mientras ambas listas tengan datos
    while i < len(izquierda) and j < len(derecha):

        # compara el valor de la tupla en la posición 2
        if izquierda[i][2] >= derecha[j][2]:

            # agrega el elemento mayor de la izquierda
            resultado.append(izquierda[i])

            # avanza en la izquierda
            i += 1

        # si el de la derecha es mayor
        else:

            # agrega el elemento de la derecha
            resultado.append(derecha[j])

            # avanza en la derecha
            j += 1

    # agrega los elementos restantes de la izquierda
    while i < len(izquierda):

        # agrega el elemento actual
        resultado.append(izquierda[i])

        # avanza en la izquierda
        i += 1

    # agrega los elementos restantes de la derecha
    while j < len(derecha):

        # agrega el elemento actual
        resultado.append(derecha[j])

        # avanza en la derecha
        j += 1

    # devuelve la lista mezclada y ordenada
    return resultado