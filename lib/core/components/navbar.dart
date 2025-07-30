
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class Navbar extends StatelessWidget implements PreferredSizeWidget {
  @override
  Size get preferredSize => Size.fromHeight(kToolbarHeight);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Text('Biovision'),
      actions: [
        TextButton(onPressed: () => context.go('/'), child: Text('Inicio')),
        TextButton(onPressed: () => context.go('/about'), child: Text('Quiénes Somos')),
        TextButton(onPressed: () => context.go('/services'), child: Text('Servicios')),
        TextButton(onPressed: () => context.go('/contact'), child: Text('Contacto')),
      ],
    );
  }
}
