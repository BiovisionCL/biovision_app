import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  const Footer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 60,
      child: Container(
        color: const Color(0xFF0B3D91),
        padding: const EdgeInsets.all(16),
        child: const Center(
          child: Text(
            '© 2025 Biovision - Todos los derechos reservados',
            style: TextStyle(color: Colors.white, fontSize: 14),
          ),
        ),
      ),
    );
  }
}