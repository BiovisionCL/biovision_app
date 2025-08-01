
import os
import sys
from pathlib import Path

def preparar_entorno_biovision():
    print("🚀 Preparando entorno Biovision...\n")
    root = Path.cwd()

    helpers_path = root / "git_helpers"
    if helpers_path.exists() and str(helpers_path) not in sys.path:
        sys.path.append(str(helpers_path))
        print("✅ Path agregado:", helpers_path)
    else:
        print("✅ Path ya estaba registrado:", helpers_path)

    try:
        from verificar_estructura_critica import verificar_estructura
        verificar_estructura()
        print("✅ Estructura crítica verificada.\n")
    except Exception as e:
        print("❌ Error al verificar estructura crítica:", e)

    try:
        from generar_landing_page_si_falta import generar_landing_page
        generar_landing_page()
        print("✅ landing_page.dart verificado o generado.\n")
    except Exception as e:
        print("❌ Error al verificar/generar landing_page.dart:", e)

    try:
        from regenerar_pubspec_yaml import regenerar_pubspec_yaml
        regenerar_pubspec_yaml()
        print("✅ pubspec.yaml regenerado con recursos declarados.\n")
    except Exception as e:
        print("❌ Error al regenerar pubspec.yaml:", e)

    try:
        from eliminar_imagenes_huerfanas import eliminar_imagenes_huerfanas
        eliminar_imagenes_huerfanas()
        print("✅ Imágenes huérfanas eliminadas.\n")
    except Exception as e:
        print("❌ Error al eliminar imágenes huérfanas:", e)

    print("🧹 Ejecutando flutter clean...\n")
    os.system("flutter clean")
    print("📦 Ejecutando flutter pub get...\n")
    os.system("flutter pub get")
    print("🌐 Ejecutando flutter run -d chrome...\n")
    os.system("flutter run -d chrome")
