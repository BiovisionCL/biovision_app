from pathlib import Path

def regenerar_pubspec_yaml():
    ruta = Path("pubspec.yaml")
    if not ruta.exists():
        print("❌ pubspec.yaml no encontrado.")
        return

    contenido = ruta.read_text(encoding="utf-8")
    if "assets/images/" in contenido:
        print("🔁 pubspec.yaml ya contiene los assets.")
        return

    nuevo = contenido.rstrip() + "\n\nflutter:\n  assets:\n    - assets/images/\n"
    ruta.write_text(nuevo, encoding="utf-8")
    print("✅ Se agregaron assets/images/ a pubspec.yaml")