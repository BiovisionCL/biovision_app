from run_cmd_function import run_cmd

def git_add_commit_push(commit_message: str) -> bool:
    """
    Ejecuta git add ., commit y push en el repo definido en run_cmd_function.

    Args:
        commit_message (str): Mensaje para el commit.

    Returns:
        bool: True si todo fue exitoso, False si falló alguna etapa.
    """
    print("[INFO] Ejecutando git add .")
    if not run_cmd(["git", "add", "."]):
        print("[ERROR] git add falló.")
        return False

    print(f"[INFO] Ejecutando git commit -m ''")
    if not run_cmd(["git", "commit", "-m", commit_message]):
        print("[WARN] git commit falló (posiblemente sin cambios). Continuando.")
        # Aquí puedes decidir si quieres devolver False o True si no hay cambios
        # Return True para continuar sin commit, o False para detener
        # Por ahora, devolvemos True para no detener el flujo
        return True

    print("[INFO] Ejecutando git push origin main")
    if not run_cmd(["git", "push", "origin", "main"]):
        print("[ERROR] git push falló.")
        return False

    print("[INFO] git add, commit y push finalizados correctamente.")
    return True
