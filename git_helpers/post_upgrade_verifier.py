import os
import re
from pathlib import Path
from datetime import datetime

PROYECTO = Path.home() / "biovision_app"
LOG = PROYECTO / "git_metadata" / f"post_upgrade_verifier_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
HOME_PAGE = PROYECTO / "lib" / "features" / "home" / "presentation" / "home_page.dart"
TESTS = [
    PROYECTO / "test" / "features" / "home" / "presentation" / "home_page_test.dart",
    PROYECTO / "test" / "widget_test.dart"
]

def log(msg):
    with open(LOG, "a") as f:
        print(msg)
        f.write(msg + "\n")

def revisar_imports():
    log("🔍 Revisando imports...")
    for file in PROYECTO.rglob("*.dart"):
        with open(file, "r") as f:
            content = f.read()
            if "package:test/test.dart" in content:
                log(f"⚠️ {file} importa test.dart, revisa compatibilidad con test_api.")
            if "package:flutter_test/flutter_test.dart" in content and "const MaterialApp(" in content:
                log(f"✅ {file} usa flutter_test correctamente con MaterialApp.")
    log("✅ Revisión de imports completada.\n")

def verificar_homepage_widgets():
    log("🧩 Verificando widgets en HomePage...")
    if not HOME_PAGE.exists():
        log("❌ No se encontró home_page.dart")
        return
    with open(HOME_PAGE, "r") as f:
        content = f.read()
    if "class HomePage extends StatelessWidget" not in content:
        log("⚠️ HomePage no está correctamente definido.")
    if "const " in content:
        pattern = re.compile(r"const\s+(MaterialApp|Scaffold|Column|Row|Text|HomePage)")
        matches = pattern.findall(content)
        if matches:
            log(f"ℹ️ Encontrados constructores const: {set(matches)}")
        else:
            log("✅ No hay problemas evidentes con const en home_page.dart")

def reparar_tests():
    log("🧪 Reparando tests con errores 'non-const'...")
    for test_file in TESTS:
        if not test_file.exists():
            log(f"⚠️ No existe {test_file.name}, omitido.")
            continue
        with open(test_file, "r") as f:
            lines = f.readlines()
        reparado = False
        for i, line in enumerate(lines):
            if "pumpWidget(const MaterialApp(home:" in line:
                lines[i] = line.replace("const ", "")
                reparado = True
                log(f"🔧 Reparado 'const' en {test_file.name}, línea {i+1}")
        if reparado:
            with open(test_file, "w") as f:
                f.writelines(lines)
            log(f"✅ Test reparado: {test_file.name}")
        else:
            log(f"✅ {test_file.name} no requería reparaciones.")

def main():
    os.makedirs(LOG.parent, exist_ok=True)
    log(f"🧪 Log de verificación post-upgrade: {LOG.name}\n")
    revisar_imports()
    verificar_homepage_widgets()
    reparar_tests()
    log("✅ Verificación post-upgrade finalizada.")

if __name__ == "__main__":
    main()
