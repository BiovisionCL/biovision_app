
import yaml
from pathlib import Path

# Ruta del archivo
pubspec_path = Path("pubspec.yaml")
backup_path = Path("pubspec_backup.yaml")
debug_log = Path("debug_pubspec_autocorrect.log")

# Leer contenido original
with open(pubspec_path, "r") as f:
    lines = f.readlines()

# Respaldar original
with open(backup_path, "w") as f:
    f.writelines(lines)

debug_msgs = []
output = []
fonts_inserted = False
assets_inserted = False

for line in lines:
    stripped = line.strip()

    if stripped.startswith("fonts:"):
        if fonts_inserted:
            debug_msgs.append("🗑️ Línea duplicada 'fonts:' eliminada.")
            continue
        fonts_inserted = True
        output.append("  fonts:\n")
        output.append("    - family: Barlow\n")
        output.append("      fonts:\n")
        output.append("        - asset: assets/fonts/Barlow-Regular.ttf\n")
        output.append("          weight: 400\n")
        output.append("        - asset: assets/fonts/Barlow-Bold.ttf\n")
        output.append("          weight: 700\n")
        debug_msgs.append("✅ Fuente Barlow añadida correctamente.")
        continue

    if "asset:" in stripped and "fonts" not in stripped:
        if assets_inserted:
            debug_msgs.append("🗑️ Línea duplicada 'assets:' eliminada.")
            continue
        assets_inserted = True
        output.append("  assets:\n")
        output.append("    - assets/images/SAT.jpg\n")
        debug_msgs.append("✅ Sección assets corregida.")
        continue

    output.append(line)

# Escribir el archivo corregido
with open(pubspec_path, "w") as f:
    f.writelines(output)

# Escribir log
with open(debug_log, "w") as f:
    for msg in debug_msgs:
        f.write(msg + "\n")

print("✅ pubspec.yaml corregido automáticamente.")
print("🪵 Debug en:", debug_log)
