import os
import re
from pathlib import Path
from datetime import datetime

ROOT = Path.home() / "biovision_app"
TESTS = list(ROOT.glob("test/**/*.dart"))
LOG = ROOT / "git_metadata" / f"test_autofix_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

def log(msg):
    print(msg)
    with open(LOG, "a") as f:
        f.write(msg + "\n")

def fix_test_file(path):
    with open(path, "r") as f:
        lines = f.readlines()

    updated = False
    fixed_lines = []

    for line in lines:
        original = line

        # 🔧 Remove invalid consts in test widgets
        line = re.sub(r'const\s+(MaterialApp|Scaffold|Column|Row|Text|HomePage)', r'\1', line)

        # 🔧 Normalize main function
        if 'void main()' in line and '@TestOn' not in "".join(lines):
            fixed_lines.insert(0, '// @dart=2.17\n')
            updated = True

        if line != original:
            updated = True
        fixed_lines.append(line)

    if updated:
        with open(path, "w") as f:
            f.writelines(fixed_lines)
        log(f"✅ Reparado: {path.relative_to(ROOT)}")
    else:
        log(f"🟢 Sin cambios: {path.relative_to(ROOT)}")

def main():
    os.makedirs(LOG.parent, exist_ok=True)
    log(f"🛠️ AUTOFIX TESTS - {datetime.now().isoformat()}\n")
    for test in TESTS:
        fix_test_file(test)
    log("\n✅ Finalizado. Revisa el log si es necesario.")

if __name__ == "__main__":
    main()
