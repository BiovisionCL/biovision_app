import 'package:flutter/material.dart';

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
