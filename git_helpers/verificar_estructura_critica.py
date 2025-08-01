# 📄 verificar_estructura_critica.py

from pathlib import Path

def verificar_estructura():
    """
    Verifica la existencia de los archivos críticos del proyecto
    y escribe un log en git_metadata/estructura_log.txt.
    """
    archivos_criticos = [
        "pubspec.yaml",
        "lib/main.dart",
        "lib/core/widgets/primary_button.dart",
        "lib/features/home/presentation/pages/home_page.dart",
        "lib/features/home/presentation/widgets/home_content.dart",
        "assets/images/SAT.jpg"
    ]

    log_path = Path("git_metadata/estructura_log.txt")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    resultados = []
    for archivo in archivos_criticos:
        ruta = Path.cwd() / archivo
        if ruta.exists():
            resultados.append(f"✅ {archivo}")
        else:
            resultados.append(f"❌ {archivo}")

    with open(log_path, "w") as f:
        for linea in resultados:
            f.write(linea + "\n")

    print("✅ Verificación completada. Revisa: git_metadata/estructura_log.txt")
    errores = [x for x in resultados if x.startswith("❌")]
    if errores:
        print("⚠️ Archivos faltantes detectados:")
        for e in errores:
            print("   ", e)
    else:
        print("🎯 Todos los archivos críticos están presentes.")