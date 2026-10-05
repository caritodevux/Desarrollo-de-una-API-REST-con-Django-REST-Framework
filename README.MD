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
-Hacer un .gitignore para el venv:
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
`git add . `(prepara los cambios nuevos)
`git commit -m "Describe lo que hiciste aquí"` (guarda localmente)
`git push` (sube a GitHub)

## Responder:
1. ¿Qué es una API?
2. ¿Qué significa REST?
3. ¿Qué diferencia existe entre GET y POST?
4. ¿Qué diferencia existe entre PUT y PATCH?
5. ¿Para qué sirve un Serializer?
6. ¿Para qué sirve un ViewSet?
7. ¿Qué función cumple un Router?
8. ¿Qué significa IsAuthenticated?
9. ¿Cuál es la diferencia entre autenticación y autorización?
10. ¿Por qué filtramos las tareas utilizando request.user?
11. ¿Qué significa el código 201?
12. ¿Qué significa el código 400?
13. ¿Qué significa el código 404?
14. ¿Por qué debemos validar los datos?
15. ¿Qué riesgos existen al implementar directamente código generado por IA?
