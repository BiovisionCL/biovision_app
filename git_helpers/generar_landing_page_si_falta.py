
from pathlib import Path

def generar_landing_page():
    ruta = Path("lib/features/landing/presentation/pages/landing_page.dart")
    if ruta.exists():
        print("🔁 landing_page.dart ya existe.")
        return

    contenido = """import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset('assets/images/fondo_agricola.jpg', fit: BoxFit.cover),
          Column(
            children: [
              AppBar(
                title: Text('Biovision'),
                backgroundColor: Colors.black87,
                actions: [
                  TextButton(onPressed: () {}, child: Text('Inicio', style: TextStyle(color: Colors.white))),
                  TextButton(onPressed: () {}, child: Text('Servicios', style: TextStyle(color: Colors.white))),
                  TextButton(onPressed: () {}, child: Text('Contacto', style: TextStyle(color: Colors.white))),
                ],
              ),
              Expanded(child: Center(child: Text("Contenido principal", style: TextStyle(color: Colors.black54)))),
              Container(
                padding: EdgeInsets.all(8),
                color: Colors.black87,
                child: Text('© 2025 Biovision. Todos los derechos reservados.', style: TextStyle(color: Colors.white)),
              )
            ],
          )
        ],
      ),
    );
  }
}
"""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido)
    print(f"✅ landing_page.dart creado en {ruta}")
