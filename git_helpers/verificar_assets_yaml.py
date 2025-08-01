
import yaml
from pathlib import Path

def verificar_y_corregir_assets():
    pubspec_path = Path("pubspec.yaml")
    if not pubspec_path.exists():
        print("❌ No se encontró pubspec.yaml")
        return

    with pubspec_path.open("r", encoding="utf-8") as f:
        content = f.read()

    if "assets/images/SAT.jpg" not in content:
        print("⚠️  Agregando assets/images/SAT.jpg al pubspec.yaml...")
        try:
            data = yaml.safe_load(content)
            if "flutter" not in data:
                data["flutter"] = {}
            if "assets" not in data["flutter"]:
                data["flutter"]["assets"] = []
            if "assets/images/SAT.jpg" not in data["flutter"]["assets"]:
                data["flutter"]["assets"].append("assets/images/SAT.jpg")
            with pubspec_path.open("w", encoding="utf-8") as f:
                yaml.dump(data, f, sort_keys=False)
            print("✅ pubspec.yaml actualizado.")
        except Exception as e:
            print(f"❌ Error al modificar pubspec.yaml: {e}")
    else:
        print("✅ Asset ya está presente en pubspec.yaml.")
