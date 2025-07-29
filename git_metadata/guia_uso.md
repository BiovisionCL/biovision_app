# Guía Práctica para Flujo Maestro del Proyecto biovision_app

Esta guía describe cómo ejecutar el flujo maestro que actualiza el repositorio Git, exporta el contexto y corre los tests automáticamente.

---

## Requisitos previos

- Tener Python y Flutter instalados y configurados.
- Tener acceso al repositorio Git y permisos para hacer push.
- Ejecutar desde la raíz del proyecto `biovision_app`.

---

## Instrucciones para ejecutar el flujo maestro

### Desde consola o terminal

python git_helpers/git_master.py

### Desde Jupyter Notebook

!python git_helpers/git_master.py

---

## Notas importantes

- El script `git_master.py` realiza:
  - `git pull` para actualizar código.
  - `git add` y `git commit` con mensajes automáticos.
  - `git push` al repositorio remoto.
  - Exporta el contexto actual a `git_metadata/context_summary.md`.
  - Ejecuta todos los tests unitarios de Flutter con `flutter test`.
  - Reporta el resultado general del flujo.

- En caso de error de autenticación en Git push, revisar configuración de token o SSH.

- Antes de migrar a una nueva ventana de desarrollo en ChatGPT o en tu entorno, ejecutar este flujo para asegurar que todo está guardado y probado.

---

## Contacto y soporte

Para cualquier duda, contactar con el equipo de desarrollo.

---