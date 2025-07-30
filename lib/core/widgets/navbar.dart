import 'package:flutter/material.dart';

class Navbar extends StatelessWidget {
  const Navbar({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 60,
      padding: const EdgeInsets.symmetric(horizontal: 24),
      color: Colors.white.withOpacity(0.95),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          const Text("RAZONBILL", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18)),
          Row(
            children: [
              TextButton(onPressed: () {}, child: const Text("Inicio")),
              TextButton(onPressed: () {}, child: const Text("Quiénes Somos")),
              TextButton(onPressed: () {}, child: const Text("Servicios")),
              TextButton(onPressed: () {}, child: const Text("Casos de Éxito")),
              TextButton(onPressed: () {}, child: const Text("Contacto")),
              ElevatedButton(onPressed: () {}, child: const Text("Ingresar")),
            ],
          ),
        ],
      ),
    );
  }
}