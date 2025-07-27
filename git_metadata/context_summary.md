# Contexto y Estado del Proyecto biovision_app
Fecha: 2025-07-27 12:23:22

Repositorio oficial: git@github.com:BiovisionCL/biovision_app.git

## Estado actual
- Tests unitarios para PrimaryButton exitosos.
- Tests Counter increments con fallos pendientes por corregir.
- Errores de Directionality en tests corregidos.
- Código desarrollado para integración de pruebas y scripts maestro git.
- Flujo de trabajo automatizado en Jupyter Notebook.

## Archivos críticos
- test/core/widgets/primary_button_test.dart
- test/core/widgets/primarybutton_test.dart
- test/features/home/presentation/home_page_test.dart
- test/widget_test.dart
- git_helpers/git_master.py (script maestro git)
- git_metadata/context_summary.md (este archivo)

## Protocolo de migración
1. Clonar o actualizar repositorio:  
   `git clone git@github.com:BiovisionCL/biovision_app.git`  
   o  
   `git pull origin main`

2. Ejecutar script maestro git_master.py para sincronización, commits y tags.

3. Ejecutar pruebas unitarias con `flutter test` y validar resultados.

4. Revisar el archivo `git_metadata/context_summary.md` para contexto actualizado.

5. Usar el prompt inicial para que la nueva ventana de ChatGPT cargue y comprenda todo el contexto y proyecto.

---

**NOTA:** Mantener siempre actualizado este archivo cada vez que se migre o haya cambios importantes.

