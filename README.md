# DevOps AD 2 - Unit Testing
Repositorio para la actividad 2 de DevOps sobre Unit Testing

## Enunciado
Se pide al alumno extender la aplicación web creada en el anterior ejercicio:\
*Se añadirán tests de tipo unitario que nos ayuden a verificar el funcionamiento de nuestros endpoints.
*Se añadirá un script que facilite la provisión del servicio, cuya invocación permite comenzar a hacer peticiones al mismo.
Para saber si nuestra batería de tests es suficiente, se utilizan herramientas de medición de cobertura, que miden qué porcentaje de nuestro código se recorre con los tests que ejecutamos.\

## Implementación
Se ha optado por realizar una implementación del servicio usando Python y Flask mediante peticiones POST y GET al servidor.\
Se ha considerado que cuando se usa el endpoint "almacena" se está modificando el estado del servidor y por tanto el verbo HTTP correcto es POST.\
Sin embargo, cuando se hace uso del endpoint "consulta", se envían datos al servidor pero no se modifica su estado, así que se ha optado por emplear GET.\
Para probar el funcionamiento se recomienda emplear un programa como Curl.

### Dependencias
* Python 3.7+
* Flask

  
### Ejecución
Para iniciar la palicación ejecutar el comando: _python server.py [-h] [-f \<filename\>] [-p \<puerto\>]_\
Si no se indica ningún parámetro se levantará el servicio con las opciones por defecto que son usando el fichero "cadenas.txt" en el puerto 12345.\
Para terminar la aplicación pulsar Ctrl+C 

Para Windows, se ha creado el fichero start.bat que inicia el servicio con sus valores por defecto

## Funcionamiento
Los dos endpoints son 
* /almacena
* /consulta

### Almacena
Para llevar a cabo el almacenamiento de una cadena en el fichero se debe realizar un POST e incluir el parámetro string con la cadena que queremos almacenar en el fichero:
* ej: _POST 127.0.0.1/almacena?string=Cadena+a+almacenar_

Si se emplea un verbo distinto de POST devolverá un error 405 Method Not Allowed.\
Si no se incluye el parámetro "string" devolverá una respuesta 400 BAD REQUEST con un json en el cuerpo con información sobre el error (debe incluir el parámetro string).
### Consulta
Para llevar a cabo la consulta de una palabra en el fichero se debe realizar un GET e incluir el parámetro string con la palabra que queremos almacenar en el fichero:
* ej: _POST 127.0.0.1/consulta?string=Cadena_

Si se emplea un verbo distinto de GET devolverá un error 405 Method Not Allowed.\
Si no se incluye el parámetro "string" devolverá una respuesta 400 BAD REQUEST con un json en el cuerpo con información sobre el error (debe incluir el parámetro string).\
Si se envía más de una palabra devolvera una respuesta 400 BAD REQUEST con un json en el cuerpo con información sobre el error (debe enviar una única palabra).

## Tests
En la carpeta tests se han incluído los test unitarios para probar el funcionamiento del servicio intentando tener una cobertura del 100%
*test_almacena.py -- prueba el funcionamiento del endpoint "almacena"
*test_consulta.py -- prueba el funcionamiento del endpoint "consulta"
*test_others.py   -- prueba el funcionamiento del resto de funciones de server.py 

Para poder ejecutar los test y ver su cobertura es necesario instalar _pytest_ y _coverage_

Para evaluar la covertura:
coverage run -m pytest
Para visualizar el resultado:
coverage report
Para generar un reporte detallado en HTML:
coverage html

## Autores ✒️

Los componentes del grupo:

* **Antonio De Gea Velasco**
* **Adrian Rodriguez Montesinos**
* **Jorge Sánchez-Alor Expósito**
