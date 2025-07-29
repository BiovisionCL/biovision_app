import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final styleTitle = Theme.of(context).textTheme.headlineMedium?.copyWith(
          fontWeight: FontWeight.bold,
          color: Colors.white,
        );
    final styleSubtitle = Theme.of(context).textTheme.bodyLarge?.copyWith(
          fontSize: 16,
          color: Colors.white70,
        );

    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(
            'assets/images/variabilidad_espacial.jpg',
            fit: BoxFit.cover,
            color: Colors.black.withOpacity(0.5),
            colorBlendMode: BlendMode.darken,
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 80),
            alignment: Alignment.centerLeft,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Datos que transforman decisiones agrícolas en resultados productivos',
                  style: styleTitle,
                ),
                const SizedBox(height: 16),
                Text(
                  'Soluciones inteligentes en agricultura de precisión, desde el terreno hasta la nube.',
                  style: styleSubtitle,
                ),
                const SizedBox(height: 32),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: Colors.black,
                    padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                  onPressed: () {
                    // Navegación futura
                  },
                  child: const Text('Explora Clima Express'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
