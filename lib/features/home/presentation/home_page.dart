import 'package:flutter/material.dart';
import '../../../core/widgets/navbar.dart';
import '../../../core/widgets/footer.dart';
import '../../../core/widgets/primary_button.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  void onExpressPressed() {
    // Acción del botón Biovision Express
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const Navbar(),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 32),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Bienvenido a Biovision',
              style: TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
                color: Color(0xFF0B3D91),
              ),
            ),
            const SizedBox(height: 24),
            PrimaryButton(
              label: 'Biovision Express',
              onPressed: onExpressPressed,
            ),
          ],
        ),
      ),
      bottomNavigationBar: const Footer(),
    );
  }
}