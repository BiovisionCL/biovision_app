def git_commit(message):
    """
    Realiza un commit en git con un mensaje especificado.

    Args:
        message (str): Mensaje del commit.

    Returns:
        bool: True si el commit fue exitoso, False en caso contrario.

    Output:
        Muestra mensajes de debug con stdout y stderr.
    """
    import subprocess
    try:
        print(f"[DEBUG] Ejecutando comando: git commit -m \"{message}\"")
        result = subprocess.run(
            ["git", "commit", "-m", message],
            cwd="/Users/fernandofuentes/biovision_app",
            text=True,
            capture_output=True,
            check=True
        )
        if result.stdout.strip():
            print(f"[STDOUT] {result.stdout.strip()}")
        if result.stderr.strip():
            print(f"[STDERR] {result.stderr.strip()}")
        print("git commit OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error ejecutando git commit: {e}")
        print(f"[STDOUT] {e.stdout}")
        print(f"[STDERR] {e.stderr}")
        return False
