import 'package:flutter/material.dart';
import '../components/navbar.dart';

class CasosExitoPage extends StatelessWidget {
  const CasosExitoPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const NavBar(),
      body: const Center(child: Text('Página Casos de Éxito')),
    );
  }
}