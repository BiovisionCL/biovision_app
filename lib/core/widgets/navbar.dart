import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class Navbar extends StatelessWidget implements PreferredSizeWidget {
  const Navbar({super.key});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.black.withOpacity(0.7),
      elevation: 0,
      title: const Text(
        'Biovision',
        style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
      ),
      actions: [
        _navItem(context, 'Inicio', '/'),
        _navItem(context, 'Quiénes Somos', '/quienes-somos'),
        _navItem(context, 'Servicios', '/servicios'),
        _navItem(context, 'Asesores', '/asesores'),
        _navItem(context, 'Casos de Éxito', '/casos'),
        _navItem(context, 'Contacto', '/contacto'),
        _navItem(context, 'Login', '/login'),
      ],
    );
  }

  Widget _navItem(BuildContext context, String title, String route) {
    return TextButton(
      onPressed: () {
        context.go(route);
      },
      child: Text(
        title,
        style: const TextStyle(color: Colors.white, fontSize: 16),
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}