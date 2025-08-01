import 'package:flutter/material.dart';
import '../components/navbar.dart';

class QuienesSomosPage extends StatelessWidget {
  const QuienesSomosPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const NavBar(),
      body: const Center(child: Text('Página Quiénes Somos')),
    );
  }
}