import 'package:flutter/material.dart';

class NavBar extends StatelessWidget implements PreferredSizeWidget {
  const NavBar({super.key});

  @override
  Size get preferredSize => const Size.fromHeight(60);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.deepPurple,
      title: Row(
        children: [
          const Text(
            'Biovision',
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 24),
          ),
          const Spacer(),
          NavBarButton(label: 'Clima Express', route: '/'),
          NavBarButton(label: 'Servicios', route: '/servicios'),
          NavBarButton(label: 'Casos de Éxito', route: '/casos_exito'),
          NavBarButton(label: 'Quiénes Somos', route: '/quienes_somos'),
        ],
      ),
    );
  }
}

class NavBarButton extends StatelessWidget {
  final String label;
  final String route;

  const NavBarButton({required this.label, required this.route, super.key});

  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: () {
        Navigator.pushNamed(context, route);
      },
      child: Text(
        label,
        style: const TextStyle(color: Colors.white, fontSize: 16),
      ),
    );
  }
}