# API REST a nivel inicial
## En los PC de INACAP:
- Desactivar los "Alias de ejecución de aplicaciones" de configuración.
- Habilitar codigo `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Instala Git, conectate a github

## Instalar en visual studio code:
- Python
- Dracula theme
- Indent rainbow
- Sql viewer

## En el proyecto creado en visual:
- Hacer un .gitignore para el venv:
```
venv/
.venv/
env/
ENV/
```

En terminal:
```terminal
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

Recuerda:
- `git add . `(prepara los cambios nuevos)
- `git commit -m "Describe lo que hiciste aquí"` (guarda localmente)
- `git push` (sube a GitHub)

## 
1. Ejecutar:
- python -m venv venv
En Windows activar el entorno utilizando:
- venv\Scripts\activate

2. Django: 
pip install django
pip install djangorestframework

3. Probar:
python manage.py runserver
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/tareas/

4. Contraseña usuarios: Clave123

## Responder:
1. ¿Qué es una API?
App Program Interface, son puentes entre aplicaciones, asi pueden comunicarse y compartir datos. Las API conectan fuentes públicas de datos con aplicaciones comerciales (ej. app de meteorologia). Más tecnicamente es un conjunto de reglas y protocolos que permite a las aplicaciones intercambiar datos, realizar accionese interactuar de manera documentada.  la API procesa la solicitud, ejecuta las acciones necesarias y devuelve una respuesta, normalmente en un formato estándar, como los definidos por JSON o XML.

2. ¿Qué significa REST?
El cliente envía las solicitudes al servidor como datos. El servidor utiliza esta entrada del cliente para iniciar funciones internas y devuelve los datos de salida al cliente. 
REST define un conjunto de funciones como GET, PUT, DELETE, etc. que los clientes pueden utilizar para acceder a los datos del servidor. Los clientes y los servidores intercambian datos mediante HTTP.
Las API REST no tienen estado,  los servidores no guardan los datos del cliente entre las solicitudes.

3. ¿Qué diferencia existe entre GET y POST?
- GET: Se utiliza para consultar o recuperar información del servidor. No debe alterar el estado de la base de datos y sus parámetros se envían visibles en la URL.
- POST: Se utiliza para enviar datos al servidor y crear un nuevo recurso. Altera el estado del sistema, los datos viajan en el cuerpo (body) de la petición y no es idempotente.

4. ¿Qué diferencia existe entre PUT y PATCH?
- PUT: Se utiliza para reemplazar por completo un recurso existente. Requiere enviar todos los campos del objeto en la petición.
- PATCH: Se utiliza para realizar actualizaciones parciales. Permite modificar únicamente los campos especificados sin afectar al resto del recurso.

5. ¿Para qué sirve un Serializer?
En Django REST Framework, convierte datos complejos (como modelos de Django o QuerySets) a formatos de intercambio como JSON o XML para enviarlos al cliente. Además, realiza la operación inversa (deserialización): recibe JSON, valida los datos según las reglas definidas y los transforma en tipos nativos de Python o instancias de modelos.

6. ¿Para qué sirve un ViewSet?
Un ViewSet abstrae y agrupa en una sola clase la lógica de las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de un recurso. En lugar de escribir métodos individuales para cada tipo de petición, define acciones como .list(), .create(), .retrieve(), .update() y .destroy().

7. ¿Qué función cumple un Router?
Un Router en DRF genera automáticamente el mapeo de URLs necesarias para un ViewSet. Conecta de forma estandarizada los métodos HTTP e IDs en la URL con las acciones correspondientes del ViewSet sin necesidad de definir cada ruta a mano en urls.py.

8. ¿Qué significa IsAuthenticated?
Es una clase de permiso en DRF que restringe el acceso a un endpoint únicamente a peticiones que contengan credenciales de usuario válidas (por ejemplo, sesiones, tokens o JWT). Si un usuario anónimo intenta acceder, la API devuelve una respuesta de rechazo.

9. ¿Cuál es la diferencia entre autenticación y autorización?
- Autenticación: Responde a "¿Quién eres?" (validar la identidad del usuario mediante credenciales).
- Autorización: Responde a "¿Qué puedes hacer?" (determinar qué permisos o recursos tiene asignados un usuario ya identificado).

10. ¿Por qué filtramos las tareas utilizando request.user?
Para garantizar el aislamiento de datos y la seguridad a nivel de usuario. Esto asegura que cada usuario solo pueda ver, modificar o eliminar las tareas que le pertenecen, evitando la fuga o manipulación no autorizada de datos de otros usuarios.

11. ¿Qué significa el código 201?
El código 201 Created indica que la petición se procesó con éxito y provocó la creación de un nuevo recurso en el servidor.

12. ¿Qué significa el código 400?
El código 400 Bad Request indica que el servidor no pudo procesar la petición debido a un error del cliente, como sintaxis inválida, campos faltantes o fallos en la validación de los datos enviados.

13. ¿Qué significa el código 404?
El código 404 Not Found indica que el recurso solicitado no existe en el servidor (la URL está mal escrita o el objeto buscado no se encuentra en la base de datos).

14. ¿Por qué debemos validar los datos?
Para asegurar la integridad de la base de datos, evitar fallos en el servidor provocados por entradas inesperadas, proteger la aplicación contra vulnerabilidades de seguridad (como inyecciones o datos maliciosos) y proveer respuestas claras al cliente cuando ingresa información incorrecta.

15. ¿Qué riesgos existen al implementar directamente código generado por IA?
- Fallas de seguridad: La IA puede sugerir código con vulnerabilidades, como falta de permisos, desinfección inadecuada de entradas o configuraciones inseguras.
- Sintaxis o métodos obsoletos/inexistentes: Puede generar alucinaciones de métodos inexistentes o utilizar versiones desactualizadas de librerías.
- Errores de contexto y estructura: El código generado puede no respetar las reglas de negocio particulares, fallar en la indentación de lenguajes como Python o crear inconsistencias con la arquitectura existente.
- Falta de mantenimiento: Si no se entiende el código que se pega, resulta sumamente difícil depurar errores cuando la aplicación falla en producción.
