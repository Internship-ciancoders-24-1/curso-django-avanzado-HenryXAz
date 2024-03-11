# Celery 
Celery es un servicio de colas de procesamiento de tareas en segundo plano, con celery podemos ejecutar tareas en segundo plano que podrían necesitar muchos recursos y demorar, este servicio nos ayuda a tener un mejor rendimiento de la aplicación y una mejor velocidad de respuesta.

## Celery flower
Es un servicio que nos permite administrar y visualizar las tareas que se han ejecutando o se están ejecutando en el servicio de celery, es importante no exponer datos sensibles para no tener filtración de información. Normalmente celery flower se ejecuta en el puerto 5555
