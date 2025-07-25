import subprocess
import os
from datetime import datetime

class GitMaster:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.restore_points_dir = os.path.join(repo_path, "git_restore_points")
        os.makedirs(self.restore_points_dir, exist_ok=True)

    def run_cmd(self, cmd_list):
        try:
            print(f"[DEBUG] Ejecutando comando: {' '.join(cmd_list)}")
            result = subprocess.run(
                cmd_list,
                cwd=self.repo_path,
                text=True,
                capture_output=True,
                check=True
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

    def git_add_commit_push(self, commit_message: str):
        print("[INFO] Ejecutando git add .")
        if not self.run_cmd(["git", "add", "."]):
            return False

        print(f"[INFO] Ejecutando git commit -m '{commit_message}'")
        commit_success = self.run_cmd(["git", "commit", "-m", commit_message])
        if not commit_success:
            print("[WARN] git commit falló (posiblemente sin cambios). Se continuará.")
            # Seguimos aunque no haya cambios nuevos, para no bloquear el flujo

        print("[INFO] Ejecutando git push origin main")
        if not self.run_cmd(["git", "push", "origin", "main"]):
            return False

        return True

    def create_tag(self, tag_name: str, message: str):
        print(f"[INFO] Creando tag '{tag_name}'")
        return self.run_cmd(["git", "tag", "-a", tag_name, "-m", message])

    def push_tags(self):
        print("[INFO] Enviando tags al remoto")
        return self.run_cmd(["git", "push", "--tags"])

    def export_tag_metadata(self, tag_name: str):
        filepath = os.path.join(self.restore_points_dir, f"tag_{tag_name}_metadata.md")
        try:
            commit_hash = subprocess.check_output(
                ["git", "rev-list", "-n", "1", tag_name],
                cwd=self.repo_path,
                text=True
            ).strip()
            commit_date = subprocess.check_output(
                ["git", "log", "-1", "--format=%cd", commit_hash],
                cwd=self.repo_path,
                text=True
            ).strip()
            author = subprocess.check_output(
                ["git", "log", "-1", "--format=%an", commit_hash],
                cwd=self.repo_path,
                text=True
            ).strip()
            changed_files = subprocess.check_output(
                ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash],
                cwd=self.repo_path,
                text=True
            ).strip().splitlines()
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Metadata del tag {tag_name}\n\n")
                f.write(f"- **Commit:** {commit_hash}\n")
                f.write(f"- **Fecha:** {commit_date}\n")
                f.write(f"- **Autor:** {author}\n")
                f.write(f"- **Archivos modificados:**\n")
                for file in changed_files:
                    f.write(f"  - {file}\n")
            print(f"[INFO] Metadatos del tag '{tag_name}' exportados en {filepath}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] No se pudo exportar metadatos: {e}")
            return False

    def add_commit_push_tag(self, commit_message: str, tag_name: str, tag_message: str):
        if not self.git_add_commit_push(commit_message):
            print("[ERROR] Falló git add, commit o push.")
            return False

        if not self.create_tag(tag_name, tag_message):
            print("[ERROR] No se pudo crear el tag.")
            return False

        if not self.push_tags():
            print("[ERROR] No se pudo enviar los tags al remoto.")
            return False

        self.export_tag_metadata(tag_name)
        return True
