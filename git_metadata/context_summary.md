# Contexto y Estado del Proyecto biovision_app
Fecha: 2025-07-27 12:35:09

Repositorio oficial: git@github.com:BiovisionCL/biovision_app.git

## Estado actual
- Tests unitarios PrimaryButton: OK.
- Tests Counter increments: Fallos pendientes.
- Errores Directionality corregidos.
- Código maestro git integrado.
- Flujo de trabajo automático desde Jupyter Notebook.

## Archivos críticos
- test/core/widgets/primary_button_test.dart
- test/core/widgets/primarybutton_test.dart
- test/features/home/presentation/home_page_test.dart
- test/widget_test.dart
- git_helpers/git_master.py
- git_metadata/context_summary.md (este archivo)

## Protocolo migración:
1. Clonar/actualizar repo:
   git clone git@github.com:BiovisionCL/biovision_app.git
   o
   git pull origin main

2. Ejecutar script maestro:
   python git_helpers/git_master.py

3. Ejecutar tests:
   flutter test

4. Leer contexto en git_metadata/context_summary.md

5. Usar prompt inicial para ventana ChatGPT nueva (generado automáticamente).

---

**IMPORTANTE:** Mantener actualizado este archivo antes de cerrar o migrar.

