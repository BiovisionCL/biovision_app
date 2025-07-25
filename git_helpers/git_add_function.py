def git_add(path="."):
    """
    Añade archivos al staging area de git.

    Args:
        path (str): Ruta o patrón de archivos a agregar (por defecto ".").

    Returns:
        bool: True si git add fue exitoso, False en caso contrario.

    Output:
        Muestra mensajes de debug con stdout y stderr.
    """
    import subprocess
    try:
        print(f"[DEBUG] Ejecutando comando: git add {path}")
        result = subprocess.run(
            ["git", "add", path],
            cwd="/Users/fernandofuentes/biovision_app",
            text=True,
            capture_output=True,
            check=True
        )
        if result.stdout.strip():
            print(f"[STDOUT] {result.stdout.strip()}")
        if result.stderr.strip():
            print(f"[STDERR] {result.stderr.strip()}")
        print("git add OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error ejecutando git add: {e}")
        print(f"[STDOUT] {e.stdout}")
        print(f"[STDERR] {e.stderr}")
        return False
