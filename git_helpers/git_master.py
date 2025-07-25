
import subprocess

def run_cmd(cmd_list):
    try:
        print(f"[DEBUG] Ejecutando comando: {' '.join(cmd_list)}")
        result = subprocess.run(
            cmd_list,
            cwd=r'/Users/fernandofuentes/biovision_app',
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

def git_add_commit_push_tag(commit_msg):
    if not commit_msg:
        print("[WARN] Mensaje de commit vacío, asignando mensaje por defecto.")
        commit_msg = "Commit automático sin mensaje"
    if not run_cmd(["git", "add", "."]):
        return False
    if not run_cmd(["git", "commit", "-m", commit_msg]):
        print("[WARN] Commit falló (posiblemente sin cambios). Continuando.")
    if not run_cmd(["git", "push", "origin", "main"]):
        return False
    # Obtener número de tag actual o crear uno nuevo incremental
    tag_base = "v1.0."
    import re
    existing_tags = subprocess.run(
        ["git", "tag"],
        cwd=r'/Users/fernandofuentes/biovision_app',
        text=True,
        capture_output=True,
    ).stdout.splitlines()
    nums = []
    for t in existing_tags:
        m = re.match(r"v1\.0\.(\d+)", t)
        if m:
            nums.append(int(m.group(1)))
    next_num = max(nums) + 1 if nums else 0
    new_tag = f"{tag_base}{next_num}"
    # Crear y pushear tag
    if run_cmd(["git", "tag", "-a", new_tag, "-m", f"Versión {new_tag} funcionalidad validada"]):
        if not run_cmd(["git", "push", "--tags"]):
            return False
    print(f"[INFO] Flujo git completo con tag '{new_tag}' realizado exitosamente.")
    return True
