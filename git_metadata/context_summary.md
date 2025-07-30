# Contexto del proyecto biovision_app
Fecha: 2025-07-29 15:47:16
Repositorio oficial: git@github.com:BiovisionCL/biovision_app.git

## Dependencias (extracto pubspec.yaml, máximo 1000 caracteres):
name: biovision_app
description: Proyecto Flutter modular Biovision
publish_to: "none"
version: 1.0.0+1

environment:
  sdk: ">=2.19.0 <3.0.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
  provider: ^6.0.5

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true

  assets:
    - assets/images/

## Archivos clave de test:
- test/core/widgets/primary_button_test.dart: Sí
- test/core/widgets/primarybutton_test.dart: Sí
- test/features/home/presentation/home_page_test.dart: Sí
- test/widget_test.dart: Sí
