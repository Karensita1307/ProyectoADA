# Proyecto Final - Matrices Dispersas
## Integrantes del grupo

| Nombre Completo                | Código     | Rol           | Correo Electrónico                        |
|--------------------------------|------------|---------------|-------------------------------------------|
| Karen Sofía López Botero       | 202459519  | Colaborador   | karen.sofia.lopez@correounivalle.edu.co   |
| Laura Sofía Echeverry González | 202477067  | Colaborador   | echeverry.laura@correounivalle.edu.co     |

---

## Descripción del proyecto

Este proyecto corresponde al problema 2 del proyecto final de la asignatura **Análisis y diseño de algoritmos I**: **procesamiento eficiente de matrices dispersas**.

El objetivo es representar una matriz de dimensiones potencialmente muy grandes, pero con pocos valores no nulos, evitando construir la matriz completa en memoria. El programa lee los datos desde un archivo plano llamado `entrada.txt`, procesa las operaciones en el orden en que aparecen y escribe los resultados en un archivo llamado `salida.txt`, tal como lo exige el enunciado del proyecto.

La solución implementa una estructura de datos propia basada en una lista enlazada simple para almacenar únicamente las posiciones no nulas de la matriz. Además, utiliza **merge sort** como estrategia de **dividir y vencer** para resolver la operación `TOP_K`, cumpliendo así uno de los requerimientos del proyecto.

---

## Operaciones soportadas

El programa soporta las operaciones principales sugeridas para el problema 2:

- `GET fila columna`
- `SET fila columna valor`
- `DELETE fila columna`
- `ROW_SUM fila`
- `COL_SUM columna`
- `REGION_SUM f1 c1 f2 c2`
- `TRANSPOSE`
- `TOP_K k`
- `DENSITY`

---

## Estructura del proyecto

```text
proyecto final/
│
├── docs/
│   └── informe.pdf
│
├── entrada/
│   └── entrada.txt
│
├── salida/
│   └── salida.txt
│
├── src/
│   ├── formateo.py
│   ├── lista_enlazada.py
│   ├── main.py
│   ├── matriz_dispersa.py
│   └── merge_sort.py
│
└── README.md
```

### Descripción breve de los archivos

- `docs/informe.pdf`: documento técnico final del proyecto.
- `main.py`: archivo principal. Ubica `entrada.txt`, llama el procesamiento y genera `salida.txt`.
- `formateo.py`: lee la entrada, procesa las operaciones y da formato a las salidas.
- `matriz_dispersa.py`: implementa la lógica de la matriz dispersa.
- `lista_enlazada.py`: contiene la estructura de datos propia usada para almacenar los elementos no nulos.
- `merge_sort.py`: contiene el algoritmo de ordenamiento usado en `TOP_K`.
- `entrada/entrada.txt`: archivo de entrada con los datos iniciales y las operaciones.
- `salida/salida.txt`: archivo de salida generado por el programa.

---

## Cómo ejecutar el programa

1. Colocar el archivo de entrada en la ruta:

```text
entrada/entrada.txt
```

2. Verificar que el archivo tenga el formato esperado para el problema 2.

3. Ejecutar el archivo principal desde la carpeta `src`:

```bash
python main.py
```

4. El programa leerá automáticamente `entrada/entrada.txt` y generará o sobrescribirá el archivo:

```text
salida/salida.txt
```

---

## Formato de entrada

El archivo `entrada.txt` debe seguir la estructura definida para el problema 2:

```text
F C N
fila columna valor
fila columna valor
...
Q
OPERACION parametros
OPERACION parametros
...
```

Donde:

- `F` es la cantidad total de filas.
- `C` es la cantidad total de columnas.
- `N` es la cantidad inicial de valores no nulos.
- `Q` es la cantidad de operaciones a procesar.

---

## Ejemplo de entrada

```text
1000000000 1000000000 6
1 1 5
1 100 7
500 300 9
1000 1000 2
200000 10 11
999999999 999999999 15
7
GET 500 300
ROW_SUM 1
COL_SUM 100
SET 1 100 20
GET 1 100
REGION_SUM 1 1 1000 1000
TOP_K 3
```

---

## Sobre el archivo de salida

No es necesario borrar manualmente `salida.txt` antes de ejecutar el programa. Si el archivo ya existe, el programa lo sobrescribe automáticamente con los nuevos resultados. Si no existe, el programa lo crea al momento de ejecutarse.

---

## Consideraciones de implementación

La solución fue diseñada para cumplir con las restricciones generales del proyecto:

- no se construye una matriz completa en memoria;
- solo se almacenan los valores no nulos;
- no se utilizan estructuras nativas prohibidas como `dict`, `set`, `sorted` o `list.sort`;
- se implementa una estructura propia de datos;
- se aplica una estrategia de dividir y vencer en una operación relevante del problema.

---