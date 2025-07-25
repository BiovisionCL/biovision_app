
import 'package:flutter/material.dart';

/// PrimaryButton es un widget reusable para botones principales.
/// Uso:
/// ```dart
/// PrimaryButton(
///   label: "Aceptar",
///   onPressed: () => print("Botón presionado"),
/// )
/// ```
class PrimaryButton extends StatelessWidget {
  final String label;
  final VoidCallback onPressed;

  const PrimaryButton({Key? key, required this.label, required this.onPressed}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      child: Text(label),
    );
  }
}
