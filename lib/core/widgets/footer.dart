import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  const Footer({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 60,
      color: Colors.black87,
      alignment: Alignment.center,
      child: const Text(
        "© 2025 Biovision | Todos los derechos reservados.",
        style: TextStyle(color: Colors.white70),
      ),
    );
  }
}