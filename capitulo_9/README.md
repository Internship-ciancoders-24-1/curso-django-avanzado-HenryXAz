# Factores a tener en cuenta al momento de desplegar una aplicación contenerizada

* Servicio vps, ejemplo: AWS
* Servicio de almacenamiento de archivos, ejemplo S3
* Contratar un dominio
* Actualizar el vps contratado
* Instalar docker en el vps
* Descargar el codigo de la aplicación desde su fuente, github por ejemplo
* Configurar las variables de entorno en función de los servicios contratados, estas varían según el proyecto ya que generalmente estamos hablando de variables que contienen valores como contraseñas o llaves de seguridads
* Construir las imágenes de docker con docker compose
* Instalar supervisord
* Crear un proceso de supervisord para poder levantar los contenedores de la aplicación mediante docker compose
* El proceso de supervisord permite ejecutar los contenedores en segundo plano y nos aseguramos de que los contenedores se levanten automáticamente en caso de existir un error
