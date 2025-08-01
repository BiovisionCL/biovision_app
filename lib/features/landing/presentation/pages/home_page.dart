
import 'package:flutter/material.dart';
import '../../../shared/widgets/navbar.dart';
import '../../../shared/widgets/footer.dart';
import 'widgets/hero_section.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const NavBar(),
      body: Column(
        children: const [
          Expanded(
            child: HeroSection(),
          ),
          Footer(),
        ],
      ),
    );
  }
}
