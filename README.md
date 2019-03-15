# MSC_Project

# Documentación

## PESOS PROMEDIO

Para el correcto funcionamiento del programa es necesario que en la carpeta raiz del programa se encuentre la carpeta "CONFIG".
Dentro de esta carpeta existen diversos archivos ".config" Estos corresponden a la configuración de cada servicio, sea (ANDES, STRING, INCA u otro).


Al correr la aplicación seleccionar la opcion 1. A continuación se mostrarán todos los archivos compatibles. (El programa buscará estos archivos tanto en la carpeta raiz como en el escritorio del usuario). Los archivos compatibles son los archivos de planos ".ASC" o los planos convertidos a ".xls" a través de la macro CASP. Una vez seleccionado el plano es necesario seleccionar el servicio correspondiente al plano. Al completar la operación se guardará el archivo resultante ".xlsx" dentro de la ruta especficiada en el archivo ".config" del servicio correspondiente y se abrirá automáticamente en Microsoft Excel.


### Nota:
- Tanto el nombre del archivo como el directorio donde se guarda no pueden contener espacios




El programa funciona de forma muy similar una tabla dinámica en excel y se ha diseñado con el propósito de ser escalable sin la necesidar de modificar mucho el codigo.


Para añadir un nuevo servicio basta con crear un nuevo archivo ".config" en la carpeta "CONFIG" y rellenar los datos correspondiente. El programa detectará automaticamente el nuevo servicio.

## FORECAST LOGISTICA

El segundo programa implementado en esta aplicación permite obtener la cantidad de bookings de ciertos despositos (solo para servicio STRING)

Para el correcto funcionamiento del programa es encesario que en la carpeta raiz del programa se encuentre la carpeta "CONFIG". Dentro de ella es necesario que exista el archivo "MAIN.config" En este archivos se puede colocar las direcciones donde se buscarán los bookings al igual que definir la ubicación donde se guardará el archivo resultante. Para ello utilizar la siguiente notación.


"save_location;directorio"

"search_location;directorio"


Ejemplo


"save_location;C:\MSC_PROJECT\OUTPUT"

"search_location;/home/matias/Desktop/MAIN_OUTPUT"


Para hacer funcionar el programa es necesario importar el booking final de la nave en cuestión.

### Nota:
- Tanto el nombre del archivo como el directorio donde se guarda no pueden contener espacios




Los depositos son los siguientes

- SAI
- SANTIAGO
- VAP
El resultado se guardará en la carpeta raiz del programa como "demo.xlsx" y se abrirá automáticamente.
