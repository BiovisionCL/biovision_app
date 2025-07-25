import subprocess
import os

REPO_PATH = os.path.expanduser("/Users/fernandofuentes/biovision_app")

def run_cmd(cmd_list):
    """
    Ejecuta un comando del sistema en la carpeta del repositorio.
    """
    try:
        print(f"[DEBUG] Ejecutando comando: {' '.join(cmd_list)}")
        result = subprocess.run(
            cmd_list,
            cwd=REPO_PATH,
            text=True,
            capture_output=True,
            check=True,
        )
        if result.stdout.strip():
            print(f"[STDOUT] {result.stdout.strip()}")
        if result.stderr.strip():
            print(f"[STDERR] {result.stderr.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error ejecutando comando: {e}")
        print(f"[STDOUT] {e.stdout}")
        print(f"[STDERR] {e.stderr}")
        return False

def git_add_commit_push(commit_message):
    """
    Ejecuta git add, commit y push para el repositorio configurado.
    """
    # git add .
    if not run_cmd(["git", "add", "."]):
        print("[ERROR] git add falló.")
        return False

    # git commit -m "mensaje"
    if not run_cmd(["git", "commit", "-m", commit_message]):
        print("[WARN] No hay cambios para commitear o commit vacío.")
        # No retornamos False porque push puede ser necesario igualmente

    # git push origin main
    if not run_cmd(["git", "push", "origin", "main"]):
        print("[ERROR] git push falló.")
        return False

    print("[INFO] git add, commit y push finalizados correctamente.")
    return True
