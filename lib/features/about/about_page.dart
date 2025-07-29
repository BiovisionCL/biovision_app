import 'package:flutter/material.dart';
import '../../core/widgets/navbar.dart';

class AboutPage extends StatelessWidget {
  const AboutPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const Navbar(),
      body: Padding(
        padding: const EdgeInsets.all(32.0),
        child: ListView(
          children: const [
            Text(
              'Quiénes Somos',
              style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 24),
            Text(
              '🚀 Misión',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            Text(
              'Desarrollar e implementar soluciones inteligentes en agricultura de precisión que generen valor agronómico real, accesible y validado para productores, asesores e inversionistas agrícolas.',
            ),
            SizedBox(height: 24),
            Text(
              '👁️ Visión',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            Text(
              'Ser la empresa de referencia en servicios agro-tecnológicos en Latinoamérica, liderando la transformación digital del agro desde el terreno con transparencia, velocidad y evidencia.',
            ),
            SizedBox(height: 24),
            Text(
              '📜 Historia',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            Text(
              'Biovision nace en la zona central de Chile como respuesta a la necesidad de traducir el lenguaje técnico de la agricultura digital en soluciones simples, accionables y con resultados medibles...',
            ),
            SizedBox(height: 24),
            Text(
              '🔍 Nuestros Valores',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            Text('• Transparencia técnica'),
            Text('• Rapidez de respuesta'),
            Text('• Sencillez operativa'),
            Text('• Escalabilidad de soluciones'),
            Text('• Compromiso con el campo'),
            SizedBox(height: 24),
            Text(
              '💬 Lideramos la transformación digital del agro desde el territorio',
              style: TextStyle(fontSize: 18, fontStyle: FontStyle.italic),
            ),
          ],
        ),
      ),
    );
  }
}