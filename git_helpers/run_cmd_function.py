def run_cmd(cmd_list):
    """
    Ejecuta un comando del sistema en la carpeta del repositorio.

    Args:
        cmd_list (list[str]): Lista con el comando y sus argumentos, e.g. ["git", "status"]

    Returns:
        bool: True si el comando fue exitoso, False en caso contrario.

    Output:
        Muestra en consola mensajes de debug con stdout y stderr.
    """
    import subprocess
    try:
        print(f"[DEBUG] Ejecutando comando: {' '.join(cmd_list)}")
        result = subprocess.run(
            cmd_list,
            cwd="/Users/fernandofuentes/biovision_app",
            text=True,
            capture_output=True,
            check=True,
        )
        if result.stdout.strip():
            print(f"[STDOUT] {{result.stdout.strip()}}")
        if result.stderr.strip():
            print(f"[STDERR] {{result.stderr.strip()}}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error ejecutando comando: {{e}}")
        print(f"[STDOUT] {{e.stdout}}")
        print(f"[STDERR] {{e.stderr}}")
        return False

