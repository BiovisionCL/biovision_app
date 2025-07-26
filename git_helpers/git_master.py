import os
import subprocess
import re

class GitMaster:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.metadata_dir = os.path.join(repo_path, "git_metadata")
        os.makedirs(self.metadata_dir, exist_ok=True)

    def run_cmd(self, cmd_list):
        try:
            print(f"[DEBUG] Ejecutando comando: {' '.join(cmd_list)}")
            result = subprocess.run(
                cmd_list,
                cwd=self.repo_path,
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

    def full_flow(self, commit_msg):
        if not commit_msg:
            print("[WARN] Mensaje de commit vacío, usando mensaje por defecto.")
            commit_msg = "Commit automático sin mensaje"

        if not self.run_cmd(["git", "add", "."]):
            return False

        if not self.run_cmd(["git", "commit", "-m", commit_msg]):
            print("[WARN] Commit falló (posiblemente sin cambios). Continuando.")

        if not self.run_cmd(["git", "push", "origin", "main"]):
            return False

        # Obtener tags existentes para generar tag incremental
        tags_res = subprocess.run(
            ["git", "tag"],
            cwd=self.repo_path,
            text=True,
            capture_output=True,
        )
        existing_tags = tags_res.stdout.splitlines()
        nums = []
        for t in existing_tags:
            m = re.match(r"v1\.0\.(\d+)", t)
            if m:
                nums.append(int(m.group(1)))
        next_num = max(nums) + 1 if nums else 0
        new_tag = f"v1.0.{next_num}"

        if self.run_cmd(["git", "tag", "-a", new_tag, "-m", f"Versión {new_tag} funcionalidad validada"]):
            if not self.run_cmd(["git", "push", "--tags"]):
                return False
        else:
            return False

        # Exportar metadatos básicos del último commit/tag
        commit_hash_res = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo_path,
            text=True,
            capture_output=True,
        )
        commit_hash = commit_hash_res.stdout.strip()

        commit_date_res = subprocess.run(
            ["git", "log", "-1", "--pretty=%cd", commit_hash],
            cwd=self.repo_path,
            text=True,
            capture_output=True,
        )
        commit_date = commit_date_res.stdout.strip()

        commit_author_res = subprocess.run(
            ["git", "log", "-1", "--pretty=%an", commit_hash],
            cwd=self.repo_path,
            text=True,
            capture_output=True,
        )
        commit_author = commit_author_res.stdout.strip()

        files_changed_res = subprocess.run(
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash],
            cwd=self.repo_path,
            text=True,
            capture_output=True,
        )
        files_changed = files_changed_res.stdout.strip().splitlines()

        metadata_path = os.path.join(self.metadata_dir, f"metadata_{new_tag}.md")
        with open(metadata_path, "w", encoding="utf-8") as f:
            f.write(f"# Metadata de commit/tag {new_tag}\n\n")
            f.write(f"- Commit: {commit_hash}\n")
            f.write(f"- Fecha: {commit_date}\n")
            f.write(f"- Autor: {commit_author}\n")
            f.write("\n**Archivos modificados:**\n")
            for file in files_changed:
                f.write(f"- {file}\n")

        print(f"[INFO] Metadatos exportados en {metadata_path}")
        print(f"[INFO] Flujo git completo con tag '{new_tag}' realizado exitosamente.")
        return True
