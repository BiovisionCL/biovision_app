
import os
import subprocess
from datetime import datetime

class GitMaster:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def run_cmd(self, cmd):
        proc = subprocess.run(cmd, shell=True, cwd=self.repo_path,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
        return proc

    def git_pull(self):
        print("Ejecutando git pull...")
        result = self.run_cmd("git pull origin main")
        if result.returncode != 0:
            print(f"[ERROR] git pull falló:\n{result.stderr}")
            return False
        print("git pull completado correctamente.")
        return True

    def git_add_commit_push(self, commit_message):
        print("Ejecutando: git add .")
        self.run_cmd("git add .")

        print(f"Ejecutando: git commit -m \"{commit_message}\"")
        commit_result = self.run_cmd(f"git commit -m \"{commit_message}\"")

        if commit_result.returncode != 0:
            if "nothing to commit" in commit_result.stderr.lower():
                print("[INFO] No hay cambios para commit, saltando commit sin error.")
            else:
                print(f"[ERROR] git commit falló:\n{commit_result.stderr}")
                return False
        else:
            print("Commit realizado con éxito.")

        print("Ejecutando: git push origin main")
        push_result = self.run_cmd("git push origin main")
        if push_result.returncode != 0:
            if "could not read Username" in push_result.stderr.lower() or                "authentication" in push_result.stderr.lower():
                print("[ERROR] git push falló por problema de autenticación. Se debe configurar token o SSH.")
                return False
            print(f"[ERROR] git push falló:\n{push_result.stderr}")
            return False

        print("Push completado con éxito.")
        return True

    def export_context(self):
        metadata_dir = os.path.join(self.repo_path, "git_metadata")
        if not os.path.exists(metadata_dir):
            os.makedirs(metadata_dir)
        context_path = os.path.join(metadata_dir, "context_summary.md")

        pubspec_path = os.path.join(self.repo_path, "pubspec.yaml")
        pubspec_content = ""
        if os.path.exists(pubspec_path):
            with open(pubspec_path, "r") as f:
                pubspec_content = f.read()

        test_files = [
            "test/core/widgets/primary_button_test.dart",
            "test/core/widgets/primarybutton_test.dart",
            "test/features/home/presentation/home_page_test.dart",
            "test/widget_test.dart"
        ]

        with open(context_path, "w") as f:
            f.write(f"# Contexto del proyecto biovision_app\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Repositorio oficial: git@github.com:BiovisionCL/biovision_app.git\n\n")
            f.write("## Dependencias (extracto pubspec.yaml, máximo 1000 caracteres):\n")
            f.write(pubspec_content[:1000] + "\n\n")
            f.write("## Archivos clave de test:\n")
            for tf in test_files:
                path = os.path.join(self.repo_path, tf)
                status = "Sí" if os.path.exists(path) else "No encontrado"
                f.write(f"- {tf}: {status}\n")

        print(f"[INFO] Contexto exportado a {context_path}")

        prompt_path = os.path.join(metadata_dir, "initial_prompt.txt")
        prompt_text = f"""Hola, soy un asistente para continuar un proyecto de Flutter llamado biovision_app.

Por favor, realiza estos pasos para preparar tu entorno:

1. Clona o actualiza el repositorio:  
   git clone git@github.com:BiovisionCL/biovision_app.git
   o si ya existe: git pull origin main

2. Abre y lee el archivo de contexto para entender el estado actual:  
   git_metadata/context_summary.md

3. Ejecuta el script maestro para sincronizar y preparar el proyecto:  
   python git_helpers/git_master.py

4. Ejecuta todas las pruebas unitarias para verificar integridad:  
   flutter test

5. Confirma que todas las pruebas pasaron sin errores.

6. Continúa con el desarrollo modular del proyecto asegurando que se mantenga la integridad y estabilidad.

Confirma cuando termines estos pasos para seguir con el desarrollo.
"""
        with open(prompt_path, "w") as f:
            f.write(prompt_text)
        print(f"[INFO] Prompt inicial guardado en {prompt_path}")

        return context_path, prompt_path

    def run_tests(self):
        print("[INFO] Ejecutando pruebas unitarias Flutter...")
        test_result = self.run_cmd("flutter test")
        print(test_result.stdout)
        if test_result.returncode != 0:
            print(f"[ERROR] Fallaron pruebas unitarias:\n{test_result.stderr}")
            return False
        print("[SUCCESS] Todas las pruebas pasaron correctamente.")
        return True

    def full_flow(self, commit_message="Commit automático desde flujo maestro completo"):
        if not self.git_pull():
            print("[ERROR] git pull falló. Continuando con precaución.")
        if not self.git_add_commit_push(commit_message):
            print("[WARN] git add/commit/push tuvo problemas pero continuamos.")
        self.export_context()
        if not self.run_tests():
            print("[ERROR] Fallaron pruebas unitarias. Deteniendo flujo.")
            return False
        print("[INFO] Flujo maestro completado exitosamente.")
        return True


if __name__ == "__main__":
    import sys
    try:
        repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    except NameError:
        repo_path = "/Users/fernandofuentes/biovision_app"

    gm = GitMaster(repo_path)
    msg = sys.argv[1] if len(sys.argv) > 1 else "Commit automático desde flujo maestro completo"
    success = gm.full_flow(msg)
    if not success:
        sys.exit(1)
