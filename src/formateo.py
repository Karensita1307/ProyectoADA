# disclaimers: largo, y muchisimos comentarios pq requiero explicar pipipi

# importa la clase principal de la matriz dispersa
from matriz_dispersa import MatrizDispersa

# lee un archivo de texto y devuelve sus líneas limpias
def leer_entrada(ruta_archivo):

    # abre el archivo en modo lectura
    archivo = open(ruta_archivo, "r")

    # lee el contenido del archivo entero
    contenido = archivo.read()

    # cierra el archivo
    archivo.close()

    # separa el contenido por líneas
    lineas_crudas = contenido.split("\n")

    # lista donde se guardarán solo las líneas útiles
    lineas_limpias = []

    # recorre todas las líneas leídas
    for linea in lineas_crudas:

        # elimina espacios al inicio y al final
        linea_limpia = linea.strip()

        # verifica que la línea no esté vacía
        if linea_limpia != "":

            # agrega la línea útil a la lista final
            lineas_limpias.append(linea_limpia)

    # devuelve la lista de líneas limpias
    return lineas_limpias


# escribe los resultados en el archivo de salida
def escribir_salida(ruta_archivo, resultados):

    # abre el archivo en modo escritura
    archivo = open(ruta_archivo, "w")

    # recorre la lista de resultados
    for i in range(len(resultados)):

        # escribe una línea de resultado
        archivo.write(resultados[i])

        # agrega salto de línea si no es la última línea
        if i < len(resultados) - 1:

            # escribe un salto de línea
            archivo.write("\n")

    # cierra el archivo
    archivo.close()


# da formato al valor de densidad
def formatear_density(valor):

    # si la densidad es exactamente cero
    if valor == 0.0:

        # devuelve el cero con decimal
        return "0.0"

    # si la densidad es muy pequeña
    if valor < 0.0001:

        # la devuelve en notación científica
        return "{:.2e}".format(valor)

    # en otro caso la redondea a 8 decimales
    return str(round(valor, 8))


# da formato a la operación get
def formatear_get(fila, columna, valor):

    # construye el texto final de salida
    return "GET " + str(fila) + " " + str(columna) + " = " + str(valor)


# da formato a la operación set
def formatear_set(fila, columna):

    # construye el texto final de salida
    return "SET " + str(fila) + " " + str(columna) + " = OK"


# da formato a la operación delete
def formatear_delete(fila, columna):

    # construye el texto final de salida
    return "DELETE " + str(fila) + " " + str(columna) + " = OK"


# da formato a la suma de una fila
def formatear_row_sum(fila, total):

    # construye el texto final de salida
    return "ROW_SUM " + str(fila) + " = " + str(total)


# da formato a la suma de una columna
def formatear_col_sum(columna, total):

    # construye el texto final de salida
    return "COL_SUM " + str(columna) + " = " + str(total)


# da formato a la suma de una región
def formatear_region_sum(f1, c1, f2, c2, total):

    # construye el texto final de salida
    return "REGION_SUM " + str(f1) + " " + str(c1) + " " + str(f2) + " " + str(c2) + " = " + str(total)


# da formato a la operación transpose
def formatear_transpose():

    # devuelve el texto fijo de la operación
    return "TRANSPOSE = OK"


# da formato a la operación top_k
def formatear_top_k(k, elementos):

    # empieza el texto con el nombre de la operación
    texto = "TOP_K " + str(k) + " ="

    # recorre los elementos del top
    for elemento in elementos:

        # toma fila, columna y valor de la tupla
        fila, columna, valor = elemento

        # agrega el elemento al texto con el formato pedido
        texto += " (" + str(fila) + "," + str(columna) + "," + str(valor) + ")"

    # devuelve el texto final
    return texto


# da formato a la operación density
def formatear_density_salida(valor):

    # convierte la densidad a un formato de texto claro
    texto_density = formatear_density(valor)

    # devuelve la línea final de salida
    return "DENSITY = " + texto_density


# procesa todas las operaciones desde la línea indicada
def procesar_operaciones(matriz, lineas, indice_inicial):

    # lee la cantidad de operaciones
    cantidad_operaciones = int(lineas[indice_inicial])

    # se mueve a la primera operación real
    indice = indice_inicial + 1

    # lista donde se guardarán los resultados
    resultados = []

    # repite según la cantidad de operaciones
    for _ in range(cantidad_operaciones):

        # separa la línea actual en partes
        partes = lineas[indice].split()

        # avanza a la siguiente línea
        indice += 1

        # toma el nombre de la operación
        operacion = partes[0]

        # caso get
        if operacion == "GET":

            # lee fila
            fila = int(partes[1])

            # lee columna
            columna = int(partes[2])

            # ejecuta la consulta
            valor = matriz.get(fila, columna)

            # guarda el resultado formateado
            resultados.append(formatear_get(fila, columna, valor))

        # caso set
        elif operacion == "SET":

            # lee fila
            fila = int(partes[1])

            # lee columna
            columna = int(partes[2])

            # lee valor
            valor = int(partes[3])

            # ejecuta la actualización
            matriz.set(fila, columna, valor)

            # guarda el resultado formateado
            resultados.append(formatear_set(fila, columna))

        # caso delete
        elif operacion == "DELETE":

            # lee fila
            fila = int(partes[1])

            # lee columna
            columna = int(partes[2])

            # ejecuta la eliminación
            matriz.delete(fila, columna)

            # guarda el resultado formateado
            resultados.append(formatear_delete(fila, columna))

        # caso row_sum
        elif operacion == "ROW_SUM":

            # lee fila
            fila = int(partes[1])

            # calcula la suma de la fila
            total = matriz.row_sum(fila)

            # guarda el resultado formateado
            resultados.append(formatear_row_sum(fila, total))

        # caso col_sum
        elif operacion == "COL_SUM":

            # lee columna
            columna = int(partes[1])

            # calcula la suma de la columna
            total = matriz.col_sum(columna)

            # guarda el resultado formateado
            resultados.append(formatear_col_sum(columna, total))

        # caso region_sum
        elif operacion == "REGION_SUM":

            # lee fila inicial
            fila_inicial = int(partes[1])

            # lee columna inicial
            columna_inicial = int(partes[2])

            # lee fila final
            fila_final = int(partes[3])

            # lee columna final
            columna_final = int(partes[4])

            # calcula la suma de la región
            total = matriz.region_sum(fila_inicial, columna_inicial, fila_final, columna_final)

            # guarda el resultado formateado
            resultados.append(formatear_region_sum(fila_inicial, columna_inicial, fila_final, columna_final, total))

        # caso transpose
        elif operacion == "TRANSPOSE":

            # ejecuta la transpuesta
            matriz.transpose()

            # guarda el resultado formateado
            resultados.append(formatear_transpose())

        # caso top_k
        elif operacion == "TOP_K":

            # lee el valor de k
            k = int(partes[1])

            # obtiene los k mayores elementos
            elementos = matriz.top_k(k)

            # guarda el resultado formateado
            resultados.append(formatear_top_k(k, elementos))

        # caso density
        elif operacion == "DENSITY":

            # calcula la densidad de la matriz
            valor_density = matriz.density()

            # guarda el resultado formateado
            resultados.append(formatear_density_salida(valor_density))

        # caso de operación desconocida
        else:

            # guarda un mensaje de error claro
            resultados.append("ERROR: operacion desconocida " + operacion)

    # devuelve todas las líneas de salida
    return resultados


# procesa un archivo completo de entrada y genera la salida
def procesar_archivo(ruta_entrada, ruta_salida):

    # lee todas las líneas limpias del archivo de entrada
    lineas = leer_entrada(ruta_entrada)

    # si el archivo está vacío, no se procesa nada
    if len(lineas) == 0:

        # devuelve false para indicar que no se pudo procesar
        return False

    # índice para recorrer las líneas
    indice = 0

    # toma la línea de encabezado
    encabezado = lineas[indice].split()

    # avanza a la siguiente línea
    indice += 1

    # lee la cantidad de filas
    filas = int(encabezado[0])

    # lee la cantidad de columnas
    columnas = int(encabezado[1])

    # lee la cantidad de valores no nulos iniciales
    cantidad_inicial = int(encabezado[2])

    # crea la matriz dispersa vacía
    matriz = MatrizDispersa(filas, columnas)

    # carga los valores iniciales
    for _ in range(cantidad_inicial):

        # separa la línea actual
        partes = lineas[indice].split()

        # avanza a la siguiente línea
        indice += 1

        # lee fila
        fila = int(partes[0])

        # lee columna
        columna = int(partes[1])

        # lee valor
        valor = int(partes[2])

        # inserta el valor inicial en la matriz
        matriz.set(fila, columna, valor)

    # procesa las operaciones restantes
    resultados = procesar_operaciones(matriz, lineas, indice)

    # escribe los resultados en el archivo de salida
    escribir_salida(ruta_salida, resultados)

    # devuelve true para indicar éxito
    return True