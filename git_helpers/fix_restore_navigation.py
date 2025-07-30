
import os
from pathlib import Path
import subprocess

project_root = Path.home() / "biovision_app"
lib_path = project_root / "lib"
features_path = lib_path / "features"
log_dir = project_root / "debug_logs"

(features_path / "home/presentation").mkdir(parents=True, exist_ok=True)
(features_path / "about/presentation").mkdir(parents=True, exist_ok=True)
log_dir.mkdir(exist_ok=True)

main_file = lib_path / "main.dart"
home_page_file = features_path / "home/presentation/home_page.dart"
about_page_file = features_path / "about/presentation/about_page.dart"

main_code = """import 'package:flutter/material.dart';
import 'features/home/presentation/home_page.dart';

void main() {
  runApp(const BiovisionApp());
}

class BiovisionApp extends StatelessWidget {
  const BiovisionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.green),
        useMaterial3: true,
      ),
      home: const HomePage(),
    );
  }
}
"""
main_file.write_text(main_code)

home_page_code = """import 'package:flutter/material.dart';
import '../../about/presentation/about_page.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text("Bienvenido a Biovision"),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const AboutPage()),
                );
              },
              child: const Text("Ver Sobre Nosotros"),
            ),
          ],
        ),
      ),
    );
  }
}
"""
home_page_file.write_text(home_page_code)

about_page_code = """import 'package:flutter/material.dart';

class AboutPage extends StatelessWidget {
  const AboutPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Sobre Biovision")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView(
          children: const [
            Text("Misión:", style: TextStyle(fontWeight: FontWeight.bold)),
            Text("Desarrollar e implementar soluciones inteligentes en agricultura de precisión."),
            SizedBox(height: 12),
            Text("Visión:", style: TextStyle(fontWeight: FontWeight.bold)),
            Text("Ser la empresa de referencia en servicios agro-tecnológicos a nivel latinoamericano."),
            SizedBox(height: 12),
            Text("Historia:", style: TextStyle(fontWeight: FontWeight.bold)),
            Text("Biovision nace en la zona central de Chile como respuesta a la creciente necesidad de integrar tecnología con visión agronómica."),
            SizedBox(height: 12),
            Text("Valores:", style: TextStyle(fontWeight: FontWeight.bold)),
            Text("- Transparencia técnica"),
            Text("- Rapidez de respuesta"),
            Text("- Sencillez operativa"),
            Text("- Compromiso"),
          ],
        ),
      ),
    );
  }
}
"""
about_page_file.write_text(about_page_code)

pub_get_log = log_dir / "flutter_pub_get.log"
with open(pub_get_log, "w") as log:
    subprocess.run(["flutter", "pub", "get"], cwd=project_root, stdout=log, stderr=log)

analyze_log = log_dir / "flutter_analyze.log"
with open(analyze_log, "w") as log:
    subprocess.run(["flutter", "analyze"], cwd=project_root, stdout=log, stderr=log)

print("✅ Restauración completa. Ejecuta ahora: %run git_helpers/fix_restore_navigation.py")
