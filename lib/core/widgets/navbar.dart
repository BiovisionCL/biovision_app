import 'package:flutter/material.dart';

class Navbar extends StatelessWidget implements PreferredSizeWidget {
  const Navbar({Key? key}) : super(key: key);

  @override
  Size get preferredSize => const Size.fromHeight(60);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: const Color(0xFF0B3D91),
      elevation: 4,
      title: const Text(
        'Biovision Express',
        style: TextStyle(
          fontWeight: FontWeight.bold,
          fontSize: 24,
          letterSpacing: 1.2,
          color: Colors.white,
        ),
      ),
      centerTitle: true,
      actions: [
        TextButton(
          onPressed: () {
            // Acción para botón Inicio
          },
          child: const Text(
            'Inicio',
            style: TextStyle(color: Colors.white, fontSize: 16),
          ),
        ),
        // Puedes agregar más botones aquí si quieres
      ],
    );
  }
}