# Projecto 3

## Parte 1

Nos piden implementar una función que reciba una velocidad dada en millas por hora y la devuelva transformada a su equivalente en kilómetros por hora.

La función se encuentra ya declarada en imperial_to_metric.py y debe de realizarse la definición.

### SOLUCIÓN

La solución es extremadamente simple. Si una milla son 1.60934, pues habrá que multiplicar las millas por hora por esa constante para obtener los kilómetros por hora. 

## Parte 2

En la sala de prensa recibimos los datos de la carrera de las 500 millas de Indianápolis. Los datos relativos a la vuelta con mayor velocidad media (en esta carrera la mejor vuelta no se representa con un tiempo, sino con una velocidad media) están en sistema imperial, que nos es extraño, y nos piden hacer un programa que automáticamente transforme la velocidad media al sistema métrico internacional.

Ir al fichero data_analysis.py, leer la documentación de la función transform_driver_race_laps e implementar la función.

### SOLUCIÓN

Recibimos una lista con los datos en millas por hora. Por lo tanto, simplemente habrá que recorrer la lista y actualizar el valor de la velocidad media.

Para ello, debemos importar la función que acabamos de hacer y que se encuentra en *imperial_to_metric.py*

```python
from imperial_to_metric import mph_to_kph
```

Posteriormente usaremos la plantilla habitual para recorrer una lista cuando no estamos interesados en la posición del elemento en la lista:

```python
for race_lap in driver_race_laps:
```

Y a cada race_lap le actualizaremos el valor invocando la función para transformar de mph a kph

```python
        race_lap["average_speed"] = mph_to_kph(race_lap["average_speed"])
```

Si os fijáis, estamos actualizando el valor dentro de la lista y devolviendo la misma lista que hemos recibido como parámetro. Esto es posible por una cualidad del parámetro, en este caso una lista, que funciona usando referencias y no copiando el valor. Esta parte queda fuera del objetivo del curso, así que no prestar atención a este detalle.

En nuestras implementaciones normalmente no hemos actualizado valores que hemos recibido, así que otra solución más en consonancia con el resto de ejercicios sería:

```python
transformed_race_laps = []
for race_lap in driver_race_laps:
    # Como nos piden devolver los mismos datos, excepto la velocidad transformada, habrá que copiar el resto de datos, en este caso el númoer de la vuelta.
    transformed_race_lap = {}
    transformed_race_lap["lap_number"] = race_lap["lap_number"]
    transformed_race_lap["average_speed"] = mph_to_kph(race_lap["average_speed"])
    transformed_race_laps.append(transformed_race_lap)

return transformed_race_laps
```

De esta forma nos ajustamos más a nuestros conocimientos:

1. Creamos una lista vacía que usaremos como resultado
2. Recorremos la lista con los datos que nos dan
3. Por cada entrada, creamos un diccionario nuevo que añadiremos en nuestro resultado.
4. A ese diccionario le añadimos todos los datos que debe tener. lap_number y average_speed, que aprovechamos a transformar como nos pide el enunciado
5. Añadimos el nuevo diccionario creado y lo metemos en la lista resultado
6. Devolvemos la lista resultado

## Parte 3

Queremos obtener la velocidad media alcanzada en una vuelta concreta.

Ir al fichero data_analysis.py, leer la documentación de la función get_lap_average_speed e implementar la función.

### SOLUCIÓN

En este ejercicio tenemos que buscar una vuelta de entre la lista de vueltas que nos dan.

Habrá que recorrer de nuevo toda la lista de vueltas y simplemente comprobar si alguna de ellas es la vuelta que nos piden, en cuyo caso la devolvemos accediendo con la clave al valor oportuno del diccionario.

```python
    for lap_info in driver_race_laps:
        if lap_info["lap_number"] == lap_number:
            return lap_info["average_speed"]
    return None
```

Importante fijarse en el enunciado, ya que nos indica que si no se encuentra ninguna vuelta con el número de vuelta que nos dan como parámetro, devolvamos None.
