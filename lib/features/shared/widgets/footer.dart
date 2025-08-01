import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  const Footer({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.black,
      padding: const EdgeInsets.all(16),
      alignment: Alignment.center,
      child: const Text(
        "© 2025 Biovisión Ingeniería América",
        style: TextStyle(color: Colors.white),
      ),
    );
  }
}