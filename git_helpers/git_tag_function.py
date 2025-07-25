def git_create_tag(tag_name, message):
    """
    Crea un tag anotado en Git con un mensaje descriptivo.

    Args:
        tag_name (str): Nombre del tag a crear, e.g. "v1.0.0".
        message (str): Mensaje descriptivo del tag.

    Returns:
        bool: True si el tag fue creado y enviado correctamente, False en caso contrario.

    Output:
        Muestra mensajes de debug con stdout y stderr.
    """
    import subprocess
    try:
        print(f"[DEBUG] Creando tag: git tag -a {tag_name} -m '{message}'")
        result_tag = subprocess.run(
            ["git", "tag", "-a", tag_name, "-m", message],
            cwd="/Users/fernandofuentes/biovision_app",
            text=True,
            capture_output=True,
            check=True
        )
        if result_tag.stdout.strip():
            print(f"[STDOUT] {result_tag.stdout.strip()}")
        if result_tag.stderr.strip():
            print(f"[STDERR] {result_tag.stderr.strip()}")

        print(f"[DEBUG] Enviando tags: git push --tags")
        result_push = subprocess.run(
            ["git", "push", "--tags"],
            cwd="/Users/fernandofuentes/biovision_app",
            text=True,
            capture_output=True,
            check=True
        )
        if result_push.stdout.strip():
            print(f"[STDOUT] {result_push.stdout.strip()}")
        if result_push.stderr.strip():
            print(f"[STDERR] {result_push.stderr.strip()}")

        print(f"Tag '{tag_name}' creado y enviado correctamente.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error creando o enviando tag: {e}")
        print(f"[STDOUT] {e.stdout}")
        print(f"[STDERR] {e.stderr}")
        return False
