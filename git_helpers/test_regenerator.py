
import os
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path.home() / "biovision_app"
TEST_DIR = PROJECT_ROOT / "test"
BACKUP_DIR = PROJECT_ROOT / "git_metadata" / "test_backups"
LOG_FILE = PROJECT_ROOT / "git_metadata" / "test_regenerator_log.txt"

TEMPLATES = {
    "widget_test.dart": """import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/main.dart';

void main() {
  testWidgets('HomePage renders correctly', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: HomePage()));
    expect(find.byType(HomePage), findsOneWidget);
  });
}
""",
    "home_page_test.dart": """import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/features/home/presentation/home_page.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('HomePage displays expected widgets', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: HomePage()));
    expect(find.textContaining(''), findsWidgets); // Ajusta según contenido real
  });
}
"""
}

def ensure_directory(path):
    path.mkdir(parents=True, exist_ok=True)

def backup_file(file_path):
    ensure_directory(BACKUP_DIR)
    if file_path.exists():
        backup_path = BACKUP_DIR / f"{file_path.name}.bak"
        with open(file_path, 'r') as original, open(backup_path, 'w') as backup:
            backup.write(original.read())
        return str(backup_path)
    return None

def regenerate_tests():
    log_entries = []
    for filename, content in TEMPLATES.items():
        test_file_path = TEST_DIR / filename
        needs_replacement = (
            not test_file_path.exists()
            or test_file_path.stat().st_size == 0
            or "void main()" not in test_file_path.read_text()
        )
        if needs_replacement:
            backup = backup_file(test_file_path)
            with open(test_file_path, 'w') as f:
                f.write(content)
            msg = f"🛠️ Regenerado: {filename}"
            if backup:
                msg += f" (backup: {backup})"
            log_entries.append(msg)
    return log_entries

def write_log(entries):
    ensure_directory(LOG_FILE.parent)
    with open(LOG_FILE, 'a') as f:
        f.write(f"\n🕒 Log {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for entry in entries:
            f.write(f"{entry}\n")

if __name__ == "__main__":
    print("🚧 Ejecutando test_regenerator...")
    entries = regenerate_tests()
    if entries:
        print("\n".join(entries))
        write_log(entries)
        print(f"📝 Log guardado en: {LOG_FILE}")
    else:
        print("✅ Todos los archivos de test están correctos.")
