
import os
from pathlib import Path
import shutil
import yaml

# Rutas clave
PROYECTO = Path.home() / "biovision_app"
IMAGEN_ORIGEN = Path.home() / "Documents" / "SAT.jpg"
DESTINO_ASSETS = PROYECTO / "assets" / "images"
PUBSPEC = PROYECTO / "pubspec.yaml"
BACKUP = PROYECTO / "pubspec_backup_assets.yaml"
DEBUG_LOG = PROYECTO / "debug_actualizacion_home.log"

# Preparar carpeta de destino
DESTINO_ASSETS.mkdir(parents=True, exist_ok=True)

# 1. Copiar imagen de fondo
try:
    destino_final = DESTINO_ASSETS / "SAT.jpg"
    shutil.copy(IMAGEN_ORIGEN, destino_final)
    msg1 = f"✅ Imagen copiada a: {destino_final}"
except Exception as e:
    msg1 = f"❌ Error al copiar la imagen: {e}"

# 2. Actualizar pubspec.yaml fusionando claves duplicadas
try:
    with open(PUBSPEC, 'r') as f:
        doc = yaml.safe_load(f)

    # Respaldar
    shutil.copy(PUBSPEC, BACKUP)

    # Normalizar assets
    assets = doc.get('flutter', {}).get('assets', [])
    if 'assets/images/SAT.jpg' not in assets:
        assets.append('assets/images/SAT.jpg')

    doc['flutter']['assets'] = sorted(set(assets))

    # Sobrescribir
    with open(PUBSPEC, 'w') as f:
        yaml.dump(doc, f, sort_keys=False)

    msg2 = "✅ pubspec.yaml actualizado correctamente."

except Exception as e:
    msg2 = f"❌ Error al actualizar pubspec.yaml: {e}"

# 3. Sobrescribir home_page.dart SIN LOGO y con SAT.jpg como fondo
try:
    HOME = PROYECTO / "lib/features/home/presentation/home_page.dart"
    HOME_BACKUP = HOME.with_name("home_page_backup.dart")
    shutil.copy(HOME, HOME_BACKUP)

    contenido = """
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(
            'assets/images/SAT.jpg',
            fit: BoxFit.cover,
          ),
          Container(
            color: Colors.black.withOpacity(0.5),
          ),
          const Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'Datos que transforman decisiones agrícolas en resultados productivos',
                  style: TextStyle(color: Colors.white, fontSize: 20),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 10),
                Text(
                  'Soluciones inteligentes en agricultura de precisión, desde el terreno hasta la nube.',
                  style: TextStyle(color: Colors.white70, fontSize: 14),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: null,
                  style: ButtonStyle(
                    backgroundColor: MaterialStatePropertyAll(Colors.greenAccent),
                  ),
                  child: Text('Explora Clima Express'),
                ),
                SizedBox(height: 40),
                Text(
                  'Tecnología que ve, mide y decide junto al campo.',
                  style: TextStyle(color: Colors.white54),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}
"""
    with open(HOME, 'w') as f:
        f.write(contenido)

    msg3 = f"✅ home_page.dart sobrescrito sin logo y con fondo SAT.jpg"

except Exception as e:
    msg3 = f"❌ Error al sobrescribir home_page.dart: {e}"

# Guardar debug
with open(DEBUG_LOG, 'w') as f:
    f.write("\n".join([msg1, msg2, msg3]))

print("🟢 ACTUALIZACIÓN COMPLETA.\n---")
print(msg1)
print(msg2)
print(msg3)
print(f"🪵 Debug en: {DEBUG_LOG}")
