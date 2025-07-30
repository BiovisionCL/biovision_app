
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
