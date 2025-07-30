
import 'package:flutter/material.dart';
import '../../../core/components/navbar.dart';
import '../../../core/components/footer.dart';

class ServicesPage extends StatelessWidget {
  final List<String> services = [
    'Levantamiento Técnico Inicial',
    'Diagnóstico agroclimático y topográfico',
    'Monitoreo Climático y Productivo',
    'Evaluación de Vigor y Estrés',
    'Predicción Hídrica Simplificada',
    'Validación de Tecnologías',
    'Informes Técnicos Interpretados',
    'Clima Express (gratuito)',
    'Biovision Asesores (plataforma exclusiva)',
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: Navbar(),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: ListView(
          children: [
            Text("Nuestros Servicios", style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
            SizedBox(height: 16),
            ...services.map((s) => ListTile(
              leading: Icon(Icons.check, color: Colors.black),
              title: Text(s),
            )),
          ],
        ),
      ),
      bottomNavigationBar: Footer(),
    );
  }
}
