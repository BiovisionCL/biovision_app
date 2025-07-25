import 'package:flutter/material.dart';
import '../../../core/widgets/navbar.dart';
import '../../../core/widgets/footer.dart';
import '../../../core/widgets/primary_button.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  void onExpressPressed() {
    // Define acción cuando el botón sea presionado
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const Navbar(),
      body: Center(
        child: PrimaryButton(
          label: 'Biovision Express',
          onPressed: onExpressPressed,
        ),
      ),
      bottomNavigationBar: const Footer(),
    );
  }
}