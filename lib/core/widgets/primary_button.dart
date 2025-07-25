import 'package:flutter/material.dart';

class PrimaryButton extends StatelessWidget {
  final String label;
  final VoidCallback onPressed;

  const PrimaryButton({
    required this.label,
    required this.onPressed,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFF0B3D91),
        elevation: 5,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
        padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 32),
      ),
      child: Text(
        label,
        style: const TextStyle(fontSize: 20, color: Colors.white, fontWeight: FontWeight.w600),
      ),
    );
  }
}