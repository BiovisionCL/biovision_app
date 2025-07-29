# Contexto del proyecto biovision_app
Fecha: 2025-07-29 11:20:14
Repositorio oficial: git@github.com:BiovisionCL/biovision_app.git

- Tests: Pasados o Pendientes
- Archivos críticos:
  - test/core/widgets/primary_button_test.dart
  - test/core/widgets/primarybutton_test.dart
  - test/features/home/presentation/home_page_test.dart
  - test/widget_test.dart
  - lib/features/home/presentation/home_page.dart
  - lib/core/widgets/primary_button.dart
  - git_helpers/git_master.py
  - Otros archivos relevantes

## Protocolo para migrar a nueva ventana ChatGPT:
1. Clonar o actualizar repo:
   git clone git@github.com:BiovisionCL/biovision_app.git  # o git pull origin main
2. Ejecutar script maestro:
   python git_helpers/git_master.py
3. Ejecutar pruebas unitarias:
   flutter test
4. Leer contexto en git_metadata/context_summary.md
5. Usar prompt inicial para nueva ventana ChatGPT
6. Continuar desarrollo modular sin perder contexto
