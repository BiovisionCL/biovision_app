from pathlib import Path

yaml_path = Path.home() / "biovision_app" / "pubspec.yaml"
backup_path = yaml_path.with_suffix(".backup.yaml")
log_path = Path.home() / "biovision_app" / "debug_pubspec_autocorrect.log"

def corregir_con_fallback():
    if not yaml_path.exists():
        raise FileNotFoundError(f"No se encontró: {yaml_path}")

    with open(yaml_path, "r") as f:
        lines = f.readlines()

    # Respaldar
    with open(backup_path, "w") as f:
        f.writelines(lines)

    log = []
    output_lines = []
    inside_fonts = False
    flutter_detected = False

    for line in lines:
        # Eliminar secciones problemáticas
        if "fonts:" in line:
            inside_fonts = True
            log.append("🗑️ Se eliminó sección 'fonts:' y contenidos.")
            continue
        if inside_fonts:
            if not line.startswith(" "):  # sale del bloque
                inside_fonts = False
            else:
                continue
        output_lines.append(line)

    # Verifica si se encuentra la clave "flutter:"
    new_output = []
    for line in output_lines:
        new_output.append(line)
        if line.strip() == "flutter:" and not flutter_detected:
            new_output.append("  uses-material-design: true\n")
            flutter_detected = True
            log.append("✅ Se agregó 'uses-material-design: true' bajo flutter.")

    # Escribir
    with open(yaml_path, "w") as f:
        f.writelines(new_output)

    with open(log_path, "w") as f:
        f.write("\n".join(log))

    print("✅ pubspec.yaml corregido y limpiado completamente.")
    print(f"🪵 Log en: {log_path}")

corregir_con_fallback()