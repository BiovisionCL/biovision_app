import subprocess

def run_cmd(cmd_list, repo_path="."):
    """
    Ejecuta un comando del sistema en la carpeta del repositorio.

    Args:
        cmd_list (list[str]): Lista con el comando y sus argumentos, e.g. ["git", "status"]
        repo_path (str): Ruta al directorio del repositorio git

    Returns:
        bool: True si el comando fue exitoso, False en caso contrario.
    """
    try:
        print(f"[DEBUG] Ejecutando comando: {' '.join(cmd_list)}")
        result = subprocess.run(
            cmd_list,
            cwd=repo_path,
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

def git_add_commit_push(commit_msg, repo_path="."):
    """
    Automatiza git add, commit y push con manejo de errores.

    Args:
        commit_msg (str): Mensaje para el commit
        repo_path (str): Ruta al repositorio git

    Returns:
        bool: True si todo fue exitoso, False en caso contrario.
    """
    # git add
    if not run_cmd(["git", "add", "."], repo_path):
        print("[WARN] git add falló")
        return False

    # git commit
    try:
        print(f"[INFO] Ejecutando git commit -m '{commit_msg}'")
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=repo_path,
            text=True,
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        # Si no hay cambios para commitear, seguimos sin fallo
        if "nothing to commit" in e.stderr.lower():
            print("[WARN] git commit falló (posiblemente sin cambios). Continuando.")
        else:
            print(f"[ERROR] git commit falló con error: {e.stderr}")
            return False

    # git push
    if not run_cmd(["git", "push", "origin", "main"], repo_path):
        print("[WARN] git push falló")
        return False

    print("[INFO] git add, commit y push finalizados correctamente.")
    return True
