import 'package:flutter/material.dart';

class FooterWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 40,
      color: Colors.black87,
      alignment: Alignment.center,
      child: Text(
        '© 2025 Biovision. Todos los derechos reservados.',
        style: TextStyle(color: Colors.white, fontSize: 12),
      ),
    );
  }
}