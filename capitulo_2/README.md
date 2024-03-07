
Las arquitecturas orientadas a servicios son denominadas SaaS(Sofwtware as a Service) y se caracterizan por la diversificación de los servicios y la agilidad del desarrollo, en el curso se estará utilizando una metodología llamada 'the twelve-factor app' que consiste en una serie de principios que se caracterizan por:

* Formas declarativas de configuración
* Un contrato claro con el SO
* Listas para lanzar
* Minimizar la diferencia entre entornos
* Fácil de escalar

Los principios son:

1. Codebase(el código debe ser versionad y debe tener una única fuente en todas las etapas de dasarrollo)
2. Dependencies(las dependencias deben ser explícitamente declaradas y deben de mantenerse privadas )
3. Configuration(Consiste en todas las credenciales, llaves, contraseñas del proyecto, la configuración no debe versionarse)
4. Backing services(servicios externos de la app como: servicio de email, servicio de colas, servico de base de datos, etc)
5. Build, release, run(No se deben de mezclar los procesos de construcción, liberación y ejecución)
6. Processes(Los procesos no deben contener estado, es decir, no debe de esperarse que un proceso almacene en memoria algo que en un futuro pueda consultar, para obtener y persistir información estan los backing services)
7. Port binding(La app es completamentea autónoma y se comunica al exterior mediante una vinculación a un puerto que escucha todas las peticiones que llegan)
8. Concurrency(Se deben tener claros los procesos. Cada tipo de trabajo debe ser ejecutado por el tipo de proceso que le corresponde, los procesos no deben de escribir archivos PID, en su lugar es mejor confiar en administradores como systemd o un administrador de procesos distribuidos en una plataforma cloud)
9. Disposability(Los procesos son desechables, deben de iniciarse o terminarse en cualquier momento y deben de responder de forma eficaz a señales de finalización)
10. Dev/prod parity(Los entornos de desarrollo y producción deben de ser lo más parecido posible para darle a los desarrolladores la capacidad de desplegar a producción)
11. Logs(La app no se preocupa del almacenamiento y administración de los logs, esta responsabilidad es delegada a los procesos y al entorno de ejecución)
12. Admin processes(Las tareas administrativas no pertenecen a la aplicación y se deben de realizar de forma independiente. Estas tareas pueden ser: backup de base de datos, eliminación de archivos obsoletos, etc)
