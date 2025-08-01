import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# Rutas
PROJECT_DIR = Path.home() / "biovision_app"
PUBSPEC = PROJECT_DIR / "pubspec.yaml"
BACKUP = PROJECT_DIR / f"pubspec_backup_upgrade_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"
LOG_FILE = PROJECT_DIR / "git_metadata/pubspec_upgrade.log"

def backup_pubspec():
    if PUBSPEC.exists():
        shutil.copy(PUBSPEC, BACKUP)
        print(f"🗂️ Respaldo creado: {BACKUP}")
    else:
        raise FileNotFoundError("❌ No se encontró el archivo pubspec.yaml")

def run_command(command, label=None):
    print(f"▶️ Ejecutando: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if label:
        with open(LOG_FILE, "a") as f:
            f.write(f"\n[{label}]\n{result.stdout}\n{result.stderr}\n")
    if result.returncode != 0:
        print(f"❌ Error en: {command}")
        print(result.stderr)
        raise RuntimeError(result.stderr)
    print(result.stdout.strip())

def upgrade_dependencies():
    print("🚀 Iniciando actualización de dependencias...")
    backup_pubspec()

    # Asegurar directorio para log
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write(f"📦 Registro de actualización - {datetime.now()}\n")

    # Upgrade general
    run_command("cd ~/biovision_app && flutter pub upgrade --major-versions", label="pub upgrade")
    
    # Verificación
    run_command("cd ~/biovision_app && flutter pub get", label="pub get")

    print(f"✅ Actualización completada. Log guardado en: {LOG_FILE}")

if __name__ == "__main__":
    try:
        upgrade_dependencies()
    except Exception as e:
        print(f"❌ Error detectado: {e}")