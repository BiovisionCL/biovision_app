# Índice de funciones git_helpers

Esta es la lista de funciones disponibles para el manejo automático de git en el proyecto.

---

## Funciones disponibles:

### run_cmd(cmd_list)
- Ejecuta un comando shell en el repositorio.
- Uso: `run_cmd(["git", "status"])`

### git_add()
- Ejecuta `git add .` para agregar todos los cambios.

### git_commit(message)
- Ejecuta `git commit -m "message"` para hacer commit con mensaje.

### git_push(remote="origin", branch="main")
- Realiza push al repositorio remoto y rama especificada.

### git_create_tag(tag_name, message)
- Crea un tag anotado con mensaje y lo sube al repositorio remoto.

---

Los archivos fuente están en la carpeta `git_helpers/` para facilitar su mantenimiento y extensión.
