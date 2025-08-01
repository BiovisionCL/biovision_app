import 'package:flutter/material.dart';
import '../components/navbar.dart';

class ServiciosPage extends StatelessWidget {
  const ServiciosPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const NavBar(),
      body: const Center(child: Text('Página Servicios')),
    );
  }
}