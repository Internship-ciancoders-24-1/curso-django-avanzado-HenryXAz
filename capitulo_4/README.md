## Serializers
Son clases que permiten instanciar objetos que manipulan y transportan datos de una capa a otra de la aplicación. Sus caracteristicas principales son:

* Parsers: Son los encargados de la validación y transformación de los datos que llegan de una petición
* Renderers: Son los encargados de devolver la respuesta en el formato que la aplicación tiene configurada; normalmente se utiliza el formato JSON

# HTTP
Http es un protocolo de comunicación, este se compone de los siguientes elementos:

* Request: Es la petición que se hace a un servidor, se compone de cabecera y cuerpo; en la cabecera se incluyen todos los metadatos necesarios que el servidor necesita para poder procesar la petición y en el cuerpo de la petición se incluyen todos los datos que queremos enviar al servidor para que los persista  o manipule

* Response: Es la respuesta que el servidor devuelve al cliente una vez procesada la petición, esta se compone de código de estado, cabecera y cuerpo de la respuesta; el código de estado indica cuál es la situación luego de haber procesado la petición, en las cabeceras se incluyen metadatos útiles para el cliente como el formato de datos que el cuerpo de la petición contiene, el origen del servidor, etc. y en el cuerpo se incluyen de ser necesarios los datos de respuesta que esta esperando el cliente.

* Códigos de estado: Permiten informarle al cliente cuál es la situación posterior al procesamiento de la petición, los códigos de estado van del 100 al 500 y significan lo siguiente:
    
    * 100-199 Procesamiento
    * 200-299 Petición exitosa
    * 300-399 Redireccionamiento
    * 400-499 Errores del cliente
    * 500-599 Errores del servidor
