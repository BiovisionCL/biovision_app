import 'package:flutter/material.dart';
import '../../../core/widgets/primary_button.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  void _onButtonPressed() {
    print("Botón presionado");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Home")),
      body: Center(
        child: PrimaryButton(
          text: "Presióname",
          onPressed: _onButtonPressed,
        ),
      ),
    );
  }
}
