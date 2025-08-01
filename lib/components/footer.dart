import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  const Footer({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.deepPurple,
      height: 60,
      child: const Center(
        child: Text(
          '© 2025 Biovision. Todos los derechos reservados.',
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}