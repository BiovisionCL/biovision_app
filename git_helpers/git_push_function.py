def git_push(remote="origin", branch="main"):
    """
    Realiza un push a un repositorio remoto y rama especificados.

    Args:
        remote (str): Nombre del repositorio remoto (default: "origin").
        branch (str): Nombre de la rama (default: "main").

    Returns:
        bool: True si el push fue exitoso, False en caso contrario.

    Output:
        Muestra mensajes de debug con stdout y stderr.
    """
    import subprocess
    try:
        print(f"[DEBUG] Ejecutando comando: git push {remote} {branch}")
        result = subprocess.run(
            ["git", "push", remote, branch],
            cwd="/Users/fernandofuentes/biovision_app",
            text=True,
            capture_output=True,
            check=True
        )
        if result.stdout.strip():
            print(f"[STDOUT] {result.stdout.strip()}")
        if result.stderr.strip():
            print(f"[STDERR] {result.stderr.strip()}")
        print("git push OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error ejecutando git push: {e}")
        print(f"[STDOUT] {e.stdout}")
        print(f"[STDERR] {e.stderr}")
        return False
