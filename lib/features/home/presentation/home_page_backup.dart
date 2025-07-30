import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: const Text('Razorbill'),
        backgroundColor: Colors.transparent,
        elevation: 0,
        actions: [
          TextButton(onPressed: () {}, child: Text('Inicio', style: TextStyle(color: Colors.white))),
          TextButton(onPressed: () {}, child: Text('Servicios', style: TextStyle(color: Colors.white))),
          TextButton(onPressed: () {}, child: Text('Contacto', style: TextStyle(color: Colors.white))),
        ],
      ),
      body: Stack(
        children: [
          Container(
            decoration: const BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/images/SAT.jpg'),
                fit: BoxFit.cover,
              ),
            ),
          ),
          Container(
            color: Colors.black.withOpacity(0.4),
          ),
          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text(
                  'Datos que transforman decisiones agrícolas en resultados productivos',
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),
                const Text(
                  'Soluciones inteligentes en agricultura de precisión, desde el terreno hasta la nube.',
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.white70, fontSize: 16),
                ),
                const SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {},
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.greenAccent,
                    foregroundColor: Colors.black,
                  ),
                  child: const Text('Explora Clima Express'),
                ),
                const SizedBox(height: 30),
                const Text(
                  'Tecnología que ve, mide y decide junto al campo.',
                  style: TextStyle(color: Colors.white54),
                ),
              ],
            ),
          ),
        ],
      ),
      bottomNavigationBar: Container(
        color: Colors.black.withOpacity(0.6),
        padding: const EdgeInsets.all(16),
        child: const Text(
          '© 2025 Razorbill. Todos los derechos reservados.',
          style: TextStyle(color: Colors.white70),
          textAlign: TextAlign.center,
        ),
      ),
    );
  }
}