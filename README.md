# FINGER 2 - VOWPAL WABBIT


## Configuración inicial

Instalar dependencias (Ubuntu 12.04)

`sudo apt-get install libboost-program-options-dev`

Para instalar VW

`git clone https://github.com/JohnLangford/vowpal_wabbit.git`

`cd vowpal_wabbit`

`make`


## Cómo correr el ejercicio

Primero necesitamos generar el archivo para el vw

`python3 get_vw_file_from_csv.py -i <input-csv> -o <output-vw>`

donde:
	-i es el archivo de entranamiento con extension csv (train.csv o data.csv)
	-o es el archivo que recibirá en su entrada el vw para predecir los resultados
	-t en el caso de querer convertir el data.csv tenemos que agregar este modificador sin parametros

Para generar el archivo de vw para el train.csv ejecutamos

`python3 get_vw_file_from_csv.py -i train.csv -o <output-train-vw>`

Lo mismo para el data.csv

`python3 get_vw_file_from_csv.py -i data.csv -o <output-test-vw>`

Luego obtenido el archivo generado haremos que el algoritmo aprenda:

`vw <output-train-vw> -c -k --passes 300 -f salida_paravw.model`

donde:
	-passes cantidad de pasadas sobre el set de entrenamiento
	-c una cache para multiples pasadas
	-k para que elimine cualquier otra cache
	-f guarda el modelo a ese archivo

Para hacer predicciones en el archivo test

`vw <output-test-vw> -t -i salida_paravw.model -p prediccion.txt`

donde:
	-t solo testea y no aprende
	-i modelo
	-p salida de predicciones

Cada línea del archivo de predicciones contendrá como primera columna el id de la review y como segunda la predicción
