import os
from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path.home() / "biovision_app"
LIB_DIR = ROOT / "lib"
GIT_META = ROOT / "git_metadata"
LOG_FILE = GIT_META / f"reparar_homepage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
ASSETS_DIR = ROOT / "assets" / "images"

HOMEPAGE_PATH = LIB_DIR / "features" / "home" / "presentation" / "home_page.dart"
NAVBAR_PATH = LIB_DIR / "core" / "widgets" / "navbar.dart"
FOOTER_PATH = LIB_DIR / "core" / "widgets" / "footer.dart"
BG_IMAGE_PATH = ASSETS_DIR / "background.jpg"

HOME_PAGE_TEMPLATE = """
import 'package:flutter/material.dart';
import 'package:biovision_app/core/widgets/navbar.dart';
import 'package:biovision_app/core/widgets/footer.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Container(
            decoration: const BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/images/background.jpg'),
                fit: BoxFit.cover,
              ),
            ),
          ),
          Column(
            children: const [
              Navbar(),
              Expanded(
                child: Center(
                  child: Text(
                    'Bienvenido a Biovision',
                    style: TextStyle(fontSize: 28, color: Colors.white),
                  ),
                ),
              ),
              Footer(),
            ],
          ),
        ],
      ),
    );
  }
}
"""

def write_file(path, content):
    if path.exists():
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        shutil.copy(path, Path(str(path) + f".bak_{timestamp}"))
    path.write_text(content.strip(), encoding='utf8')

with open(LOG_FILE, "w") as log:
    log.write("🔧 REPARACIÓN HOME PAGE - Biovision App\n")
    log.write(f"🕓 {datetime.now()}\n\n")

    if not BG_IMAGE_PATH.exists():
        log.write(f"❌ Fondo no encontrado: {BG_IMAGE_PATH}\n")
    else:
        log.write("✅ Fondo encontrado correctamente.\n")

    write_file(HOMEPAGE_PATH, HOME_PAGE_TEMPLATE)
    log.write(f"✅ Restaurado: {HOMEPAGE_PATH.name}\n")

    if not NAVBAR_PATH.exists():
        log.write(f"⚠️ Navbar ausente: {NAVBAR_PATH}\n")
    else:
        log.write(f"✅ Navbar presente: {NAVBAR_PATH.name}\n")

    if not FOOTER_PATH.exists():
        log.write(f"⚠️ Footer ausente: {FOOTER_PATH}\n")
    else:
        log.write(f"✅ Footer presente: {FOOTER_PATH.name}\n")

    log.write("\n✅ Reparación completa.\n")