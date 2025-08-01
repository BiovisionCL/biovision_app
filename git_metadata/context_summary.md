# Contexto del proyecto biovision_app
Fecha: 2025-07-29 23:25:09
Repositorio oficial: git@github.com:BiovisionCL/biovision_app.git

## Dependencias (extracto pubspec.yaml, máximo 1000 caracteres):
name: biovision_app
description: Proyecto Flutter para Biovision.
publish_to: "none"

version: 1.0.0+1

environment:
  sdk: ">=3.1.0 <4.0.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
  google_fonts: ^6.1.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true


## Archivos clave de test:
- test/core/widgets/primary_button_test.dart: Sí
- test/core/widgets/primarybutton_test.dart: Sí
- test/features/home/presentation/home_page_test.dart: Sí
- test/widget_test.dart: Sí
## 🛠️ Mejora automática - 2025-07-30 00:20:33
- Se agregó verificación automática de errores en `pubspec.yaml` dentro de `git_master.py`.
- Si el archivo está dañado, se ejecuta automáticamente `regenerar_pubspec()` y se reintenta `flutter pub get`.
- Esto hace que el entorno sea más robusto y tolerante a fallos.

