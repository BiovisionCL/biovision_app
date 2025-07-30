import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Row(
          children: [
            Image.asset(
              'assets/images/razorbill_logo.jpg',
              height: 32,
              errorBuilder: (context, error, stackTrace) =>
                  const Icon(Icons.image_not_supported, color: Colors.white),
            ),
            const SizedBox(width: 8),
            const Text(
              'Razorbill',
              style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        actions: [
          TextButton(onPressed: () {}, child: const Text("Inicio", style: TextStyle(color: Colors.white))),
          TextButton(onPressed: () {}, child: const Text("Servicios", style: TextStyle(color: Colors.white))),
          TextButton(onPressed: () {}, child: const Text("Contacto", style: TextStyle(color: Colors.white))),
          const SizedBox(width: 10),
        ],
      ),
      body: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(
            'assets/images/SAT.jpg',
            fit: BoxFit.cover,
            errorBuilder: (context, error, stackTrace) =>
                const Center(child: Text("No se pudo cargar la imagen de fondo", style: TextStyle(color: Colors.white))),
          ),
          Container(
            color: Colors.black.withOpacity(0.5),
          ),
          Center(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 32),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    'Datos que transforman decisiones agrícolas en resultados productivos',
                    style: TextStyle(fontSize: 28, color: Colors.white, fontWeight: FontWeight.bold),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 12),
                  const Text(
                    'Soluciones inteligentes en agricultura de precisión, desde el terreno hasta la nube.',
                    style: TextStyle(fontSize: 16, color: Colors.white70),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 24),
                  ElevatedButton(
                    onPressed: () {},
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.greenAccent,
                      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                    ),
                    child: const Text('Explora Clima Express', style: TextStyle(color: Colors.black)),
                  ),
                  const SizedBox(height: 40),
                  const Text(
                    'Tecnología que ve, mide y decide junto al campo.',
                    style: TextStyle(fontSize: 14, color: Colors.white60),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
      bottomNavigationBar: Container(
        padding: const EdgeInsets.all(12),
        color: Colors.grey[900],
        child: const Text(
          '© 2025 Razorbill. Todos los derechos reservados.',
          textAlign: TextAlign.center,
          style: TextStyle(color: Colors.white70, fontSize: 12),
        ),
      ),
    );
  }
}
