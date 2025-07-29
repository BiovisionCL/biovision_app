import 'package:flutter/material.dart';

class AboutPage extends StatelessWidget {
  const AboutPage({super.key});

  @override
  Widget build(BuildContext context) {
    final styleTitle = Theme.of(context).textTheme.titleLarge?.copyWith(
          fontWeight: FontWeight.w700,
          fontSize: 28,
        );
    final styleBody = Theme.of(context).textTheme.bodyLarge?.copyWith(
          fontSize: 16,
        );

    return Scaffold(
      appBar: AppBar(
        title: const Text('Quiénes Somos'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: ListView(
          children: [
            Text('🚀 Misión', style: styleTitle),
            const SizedBox(height: 8),
            Text(
              'Desarrollar e implementar soluciones inteligentes en agricultura de precisión que generen valor agronómico real, accesible y validado para productores, asesores e inversionistas agrícolas.',
              style: styleBody,
            ),
            const SizedBox(height: 24),
            Text('🎯 Visión', style: styleTitle),
            const SizedBox(height: 8),
            Text(
              'Ser la empresa de referencia en servicios agro-tecnológicos en Latinoamérica, liderando la transformación digital del agro desde el terreno con transparencia, velocidad y evidencia.',
              style: styleBody,
            ),
            const SizedBox(height: 24),
            Text('📜 Historia', style: styleTitle),
            const SizedBox(height: 8),
            Text(
              'Biovision nace en la zona central de Chile como respuesta a la necesidad de traducir el lenguaje técnico de la agricultura digital en soluciones simples, accionables y con resultados medibles.',
              style: styleBody,
            ),
            const SizedBox(height: 24),
            Text('💡 Nuestros Valores', style: styleTitle),
            const SizedBox(height: 8),
            ...[
              'Transparencia técnica',
              'Rapidez de respuesta',
              'Sencillez operativa',
              'Escalabilidad de soluciones',
              'Compromiso con el campo',
            ].map((value) => Padding(
                  padding: const EdgeInsets.symmetric(vertical: 2),
                  child: Row(
                    children: [
                      const Icon(Icons.check_circle_outline, size: 18, color: Colors.greenAccent),
                      const SizedBox(width: 8),
                      Expanded(child: Text(value, style: styleBody)),
                    ],
                  ),
                )),
            const SizedBox(height: 24),
            Row(
              children: [
                const Icon(Icons.chat_bubble_outline, color: Colors.white70),
                const SizedBox(width: 8),
                Text(
                  'Lideramos la transformación digital del agro desde el territorio',
                  style: styleBody?.copyWith(fontStyle: FontStyle.italic),
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}
