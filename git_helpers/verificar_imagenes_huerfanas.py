import os
import yaml

def verificar_imagenes_huerfanas():
    project_root = os.path.expanduser("~/biovision_app")
    assets_dir = os.path.join(project_root, "assets", "images")
    pubspec_path = os.path.join(project_root, "pubspec.yaml")
    log_path = os.path.join(project_root, "git_metadata", "imagenes_huerfanas.txt")

    try:
        with open(pubspec_path, "r") as f:
            pubspec = yaml.safe_load(f)
        declared_assets = pubspec.get("flutter", {}).get("assets", [])
    except Exception as e:
        print(f"❌ Error leyendo pubspec.yaml: {e}")
        return

    # Listar archivos reales en la carpeta
    try:
        actual_images = set(os.listdir(assets_dir))
    except Exception as e:
        print(f"❌ No se pudo acceder a la carpeta de imágenes: {e}")
        return

    # Archivos referenciados
    referenced = set()
    for asset in declared_assets:
        if asset.startswith("assets/images/"):
            referenced.add(asset.split("/")[-1])

    # Comparar
    huérfanas = actual_images - referenced

    # Escribir log
    with open(log_path, "w") as f:
        if huérfanas:
            f.write("⚠️ Imágenes huérfanas detectadas:\n")
            for img in sorted(huérfanas):
                f.write(f"- {img}\n")
        else:
            f.write("✅ No se detectaron imágenes huérfanas.\n")

    print(f"🧹 Revisión de imágenes huérfanas completada. Revisa: {log_path}")