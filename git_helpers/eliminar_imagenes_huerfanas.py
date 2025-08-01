
from pathlib import Path

def eliminar_imagenes_huerfanas():
    carpeta = Path("assets/images")
    if not carpeta.exists():
        print("❌ Carpeta assets/images no existe.")
        return

    usadas = set()
    for archivo in Path("lib").rglob("*.dart"):
        try:
            for line in archivo.read_text(errors="ignore").splitlines():
                if "assets/images/" in line:
                    try:
                        fragmento = line.split("assets/images/")[1].split("'")[0].strip()
                        if fragmento:
                            usadas.add(fragmento)
                    except IndexError:
                        continue
        except Exception as e:
            print(f"⚠️ Error al leer {archivo.name}: {e}")

    eliminadas = 0
    for imagen in carpeta.glob("*"):
        if imagen.name not in usadas:
            print(f"🗑️ Eliminando {imagen.name}")
            imagen.unlink()
            eliminadas += 1

    print(f"✅ Eliminación completa. {eliminadas} imagen(es) eliminadas.")
