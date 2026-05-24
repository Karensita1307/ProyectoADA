# importa el módulo para manejar rutas de archivos
import os

# importa la función principal que procesa el archivo
from formateo import procesar_archivo


# función principal del programa
def main():

    # obtiene la carpeta donde está este archivo
    carpeta_src = os.path.dirname(os.path.abspath(__file__))

    # obtiene la carpeta raíz del proyecto
    carpeta_proyecto = os.path.dirname(carpeta_src)

    # construye la ruta del archivo de entrada
    ruta_entrada = os.path.join(carpeta_proyecto, "entrada", "entrada.txt")

    # construye la ruta del archivo de salida
    ruta_salida = os.path.join(carpeta_proyecto, "salida", "salida.txt")

    # verifica si el archivo de entrada existe
    if not os.path.exists(ruta_entrada):

        # muestra un mensaje de error claro
        print("error: no se encontró el archivo entrada.txt")

        # termina la ejecución de la función
        return

    # procesa el archivo de entrada y genera la salida
    exito = procesar_archivo(ruta_entrada, ruta_salida)

    # verifica si el archivo estaba vacío o no pudo procesarse
    if not exito:

        # muestra un mensaje de error claro
        print("error: el archivo de entrada está vacío o no se pudo procesar")

        # termina la ejecución
        return

    # avisa que el proceso terminó bien
    print("proceso completado. revisa el archivo salida.txt")


# verifica si este archivo se está ejecutando directamente
if __name__ == "__main__":

    # llama a la función principal
    main()